from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(str, Enum):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    username = Column(String(256), nullable=False, unique=True)
    password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    role = Column(String(length=50), default=str(Role.USER))

    registered_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now()
    )

    posts = relationship('Post', back_populates='user')
    likes = relationship('Like', back_populates='user')


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String(256), nullable=False)

    user = relationship('User', back_populates='posts')
    likes = relationship('Like', back_populates='post')


class Like(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    user = relationship('User', back_populates='likes')
    post = relationship('Post', back_populates='likes')
