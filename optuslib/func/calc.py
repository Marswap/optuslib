from .time import timestamp_point
from ..schemas.dashboard.charts import PairSequence
from ..schemas.dashboard.db.operation import Operation


def operation_is_swap(
    operation: Operation,
) -> bool:
    if operation.operation_type:
        return operation.operation_type.name == "swap"
    else:
        return (
            operation.token_0_amount > 0
            and operation.token_1_amount < 0
            or operation.token_0_amount < 0
            and operation.token_1_amount > 0
        )


def get_start_time(
    seq: PairSequence,
    default: int,
) -> int | None:
    return min(seq.token_0.keys(), default=default)


def calc_liquidity_change(
    operations: list[Operation],
    time_interval: int,
) -> dict[int, PairSequence]:
    changes: dict[int, PairSequence] = {}

    for operation in operations:
        day = timestamp_point(operation.timestamp, time_interval)

        if operation.pool.id not in changes:
            changes[operation.pool.id] = PairSequence()

        changes[operation.pool.id].token_0[day] = (
            changes[operation.pool.id].token_0.get(day, 0) + operation.token_0_amount
        )

        changes[operation.pool.id].token_1[day] = (
            changes[operation.pool.id].token_1.get(day, 0) + operation.token_1_amount
        )

    return changes


def calc_volume_change(
    operations: list[Operation],
    time_interval: int,
) -> dict[int, PairSequence]:
    changes: dict[int, PairSequence] = {}

    for operation in operations:
        if operation_is_swap(operation):
            day = timestamp_point(operation.timestamp, time_interval)

            if operation.pool.id not in changes:
                changes[operation.pool.id] = PairSequence()

            changes[operation.pool.id].token_0[day] = changes[operation.pool.id].token_0.get(day, 0) + abs(
                operation.token_0_amount
            )

            changes[operation.pool.id].token_1[day] = changes[operation.pool.id].token_1.get(day, 0) + abs(
                operation.token_1_amount
            )

    return changes


def calc_swap_count_change(
    operations: list[Operation],
    time_interval: int,
) -> dict[int, dict[int, int]]:
    change: dict[int, dict[int, int]] = {}

    for operation in operations:
        if operation.pool.id not in change:
            change[operation.pool.id] = {}

        if operation_is_swap(operation):
            day = timestamp_point(operation.timestamp, time_interval)

            change[operation.pool.id][day] = change[operation.pool.id].get(day, 0) + 1

    return change


def calc_liquidity_sequence(
    liquidity_changes: dict[int, PairSequence],
    now_timestamp: int,
    time_interval: int,
) -> dict[int, PairSequence]:
    liquidity: dict[int, PairSequence] = {}

    for pool_id, changes in liquidity_changes.items():
        liquidity[pool_id] = PairSequence()

        start_time = get_start_time(changes, now_timestamp)

        for day in range(start_time, now_timestamp, time_interval):
            liquidity[pool_id].token_0[day] = liquidity[pool_id].token_0.get(
                day - time_interval, 0
            ) + changes.token_0.get(day, 0)

            liquidity[pool_id].token_1[day] = liquidity[pool_id].token_1.get(
                day - time_interval, 0
            ) + changes.token_1.get(day, 0)

    return liquidity
