from sqlalchemy.orm import Session
from src.db.models import User

class AuthService:
    @staticmethod
    async def user_exists(username: str, db: Session):
        query = db.query(User).filter(User.username == username)
        user = query.one_or_none()
        return user or None

    @staticmethod
    async def create_user(username: str, password: str, email: str, db: Session):
        user = User(username=username, password=password, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user