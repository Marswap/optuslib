from ..storages.redis import RedisStorage


async def create_fast_storage(url: str):
    return RedisStorage(url=url)
