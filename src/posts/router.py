from fastapi import APIRouter, Depends, HTTPException
from redis.client import Redis
from sqlalchemy.orm import Session

from src.cache.redis_connection import get_redis_client
from src.db.models import Post
from src.posts.services import PostService
from src.schemas.post_schema import PostCreate, PostUpdate, PostContent
from src.auth.jwt_auth import AuthHandler
from src.db.database import get_db
from fastapi_cache.decorator import cache

posts_router = APIRouter()

auth_handler = AuthHandler()


@posts_router.post('/posts', tags=["posts"])
def create_post(
        post_data: PostCreate,
        db: Session = Depends(get_db),
        user=Depends(auth_handler.auth_wrapper)
):
    post = PostService.create_post(db, user, post_data)
    return {"message": "Post has been created successfully"}


@posts_router.put("/posts/{post_id}", tags=["posts"])
def update_post(
        post_id: int,
        post_data: PostUpdate,
        db: Session = Depends(get_db),
        user=Depends(auth_handler.auth_wrapper)
):
    post = PostService.update_post(db, post_id, post_data, user)
    return {"message": "Post has been updated successfully"}


@posts_router.delete("/posts/{post_id}", tags=["posts"])
def delete_post(
        post_id: int,
        db: Session = Depends(get_db),
        user=Depends(auth_handler.auth_wrapper)
):
    post = PostService.delete_post(db, post_id, user)
    return {"message": "Post has been deleted successfully"}


@posts_router.get("/posts/{post_id}", tags=["posts"], response_model=PostContent)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {"content": post.content}


@posts_router.post("/posts/{post_id}/like", tags=["likes"])
def like_post(
        post_id_val: int,
        flag: bool,
        db: Session = Depends(get_db),
        user=Depends(auth_handler.auth_wrapper),
        redis: Redis = Depends(get_redis_client),
):
    return PostService.like_or_unlike_post(db, post_id_val, flag, user, redis)
