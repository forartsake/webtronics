from fastapi import APIRouter, Depends
from redis import Redis
from src.cache.redis_connection import get_redis_client
cache_router = APIRouter()

@cache_router.get("/likes", tags=["likes"])
def get_liked_posts(user_id: int, redis: Redis = Depends(get_redis_client)):
    liked_posts = redis.smembers(f"liked_posts:{user_id}")
    return {"liked_posts": list(liked_posts)}


@cache_router.get("/dislikes", tags=["likes"])
def get_disliked_posts(user_id: int, redis: Redis = Depends(get_redis_client)):
    disliked_posts = redis.smembers(f"disliked_posts:{user_id}")
    return {"disliked_posts": list(disliked_posts)}