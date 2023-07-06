from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.db.models import Post, User, Like
from src.schemas.post_schema import PostCreate, PostUpdate


class PostService:
    @staticmethod
    def create_post(db: Session, user: User, post_data: PostCreate):
        try:
            post = Post(user_id=user, content=post_data.content)
            db.add(post)
            db.commit()
            db.refresh(post)
            return post
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail="Failed to create post")

    @staticmethod
    def update_post(db: Session, post_id: int, post_data: PostUpdate, user: User):
        post = db.query(Post).filter(Post.id == post_id).first()

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        if post.user_id != user:
            raise HTTPException(status_code=403, detail="You are not the owner of this post")

        try:
            post.content = post_data.content
            db.commit()

        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail="Failed to update post")

    @staticmethod
    def delete_post(db: Session, post_id: int, user: User):
        post = db.query(Post).filter(Post.id == post_id).first()

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        if post.user_id != user:
            raise HTTPException(status_code=403, detail="You cannot perform such action")

        try:
            db.delete(post)
            db.commit()

        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail="Failed to update post")

    @staticmethod
    def like_or_unlike_post(db: Session, post_id: int, flag: bool, user_id: int) -> str:
        post = db.query(Post).filter(Post.id == post_id).first()

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        if post.user_id == user_id:
            raise HTTPException(status_code=403, detail="You cannot like your own post")

        existing_like = (
            db.query(Like)
            .filter(Like.user_id == user_id, Like.post_id == post_id)
            .first()
        )

        if flag:
            if existing_like:
                raise HTTPException(status_code=400, detail="You have already liked this post")

            new_like = Like(user_id=user_id, post_id=post_id)
            db.add(new_like)
            db.commit()
            db.refresh(new_like)
            return "Post liked successfully"
        else:
            if not existing_like:
                raise HTTPException(status_code=400, detail="You have not liked this post before")

            db.delete(existing_like)
            db.commit()
            return "Post has been deleted successfully"
