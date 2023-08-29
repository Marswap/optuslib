from datetime import datetime, timezone

from ..constants import USD_LIQUIDITY_ROUND_DECIMALS, USD_VOLUME_ROUND_DECIMALS
from .time import timestamp_point
from ..schemas.dashboard.charts import PairSequence, ChartPoint
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


def calc_liquidity_sequence_map(
    operations: list[Operation],
    time_interval: int,
    now_timestamp: int,
) -> dict[int, PairSequence]:
    change_seq_map: dict[int, PairSequence] = {}

    for operation in operations:
        time_key = timestamp_point(operation.timestamp, time_interval)

        if operation.pool.id not in change_seq_map:
            change_seq_map[operation.pool.id] = PairSequence()

        change_seq_map[operation.pool.id].token_0[time_key] = (
            change_seq_map[operation.pool.id].token_0.get(time_key, 0) + operation.token_0_amount
        )

        change_seq_map[operation.pool.id].token_1[time_key] = (
            change_seq_map[operation.pool.id].token_1.get(time_key, 0) + operation.token_1_amount
        )

    liquidity_seq_map: dict[int, PairSequence] = {}

    for pool_id, change_seq in change_seq_map.items():
        liquidity_seq_map[pool_id] = PairSequence()

        start_time = get_start_time(change_seq, now_timestamp)

        for time_key in range(start_time, now_timestamp, time_interval):
            liquidity_seq_map[pool_id].token_0[time_key] = liquidity_seq_map[pool_id].token_0.get(
                time_key - time_interval, 0
            ) + change_seq.token_0.get(time_key, 0)

            liquidity_seq_map[pool_id].token_1[time_key] = liquidity_seq_map[pool_id].token_1.get(
                time_key - time_interval, 0
            ) + change_seq.token_1.get(time_key, 0)

    return liquidity_seq_map


def calc_volume_sequence_map(
    operations: list[Operation],
    time_interval: int,
    now_timestamp: int,
) -> dict[int, PairSequence]:
    change_seq_map: dict[int, PairSequence] = {}

    for operation in operations:
        if operation_is_swap(operation):
            time_key = timestamp_point(operation.timestamp, time_interval)

            if operation.pool.id not in change_seq_map:
                change_seq_map[operation.pool.id] = PairSequence()

            change_seq_map[operation.pool.id].token_0[time_key] = change_seq_map[operation.pool.id].token_0.get(
                time_key, 0
            ) + abs(operation.token_0_amount)

            change_seq_map[operation.pool.id].token_1[time_key] = change_seq_map[operation.pool.id].token_1.get(
                time_key, 0
            ) + abs(operation.token_1_amount)

    volume_seq_map: dict[int, PairSequence] = {}

    for pool_id, change_seq in change_seq_map.items():
        volume_seq_map[pool_id] = PairSequence()

        start_time = get_start_time(change_seq, now_timestamp)

        for time_key in range(start_time, now_timestamp, time_interval):
            volume_seq_map[pool_id].token_0[time_key] = change_seq.token_0.get(time_key, 0)

            volume_seq_map[pool_id].token_1[time_key] = change_seq.token_1.get(time_key, 0)

    return volume_seq_map


def calc_swaps_sequence_map(
    operations: list[Operation],
    time_interval: int,
    now_timestamp: int,
) -> dict[int, dict[int, int]]:
    change_seq_map: dict[int, dict[int, int]] = {}

    for operation in operations:
        if operation.pool.id not in change_seq_map:
            change_seq_map[operation.pool.id] = {}

        if operation_is_swap(operation):
            time_key = timestamp_point(operation.timestamp, time_interval)

            change_seq_map[operation.pool.id][time_key] = change_seq_map[operation.pool.id].get(time_key, 0) + 1

    swaps_seq_map: dict[int, dict[int, int]] = {}

    for pool_id, change_seq in change_seq_map.items():
        swaps_seq_map[pool_id] = {}

        start_time = get_start_time(change_seq, now_timestamp)

        for time_key in range(start_time, now_timestamp, time_interval):
            swaps_seq_map[pool_id][time_key] = change_seq(time_key, 0)

    return swaps_seq_map


def value_with_decimals(value: int, decimals: int) -> float:
    return value / 10**decimals


def calc_liquidity_chart(liquidity_seq: dict[int, float]) -> list[ChartPoint]:
    return calc_chart(liquidity_seq, USD_LIQUIDITY_ROUND_DECIMALS)


def calc_volume_chart(volume_seq: dict[int, float]) -> list[ChartPoint]:
    return calc_chart(volume_seq, USD_VOLUME_ROUND_DECIMALS)


def calc_swaps_chart(swaps_seq: dict[int, int]) -> list[ChartPoint]:
    return calc_chart(swaps_seq)


def calc_chart(seq: dict[int, float] | dict[int, int], decimals: int | None = None) -> list[ChartPoint]:
    return [
        ChartPoint(
            time=datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%d"),
            value=value if decimals is None else round(value, decimals),
        )
        for timestamp, value in sorted(seq.items())
    ]
