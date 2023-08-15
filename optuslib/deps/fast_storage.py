from ..storages.redis import RedisStorage


async def get_fast_storage():
    fast_storage = RedisStorage()
    try:
        yield fast_storage
    finally:
        await fast_storage.close()
