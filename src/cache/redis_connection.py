import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB


def get_redis_client():
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    try:
        yield redis_client
    finally:
        redis_client.close()
