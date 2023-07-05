from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.auth.jwt_auth import AuthHandler
from src.schemas.user_schema import UserCreate, UserLogin
from src.auth.services import AuthService
from src.db.database import get_db

auth_router = APIRouter()
auth_handler = AuthHandler()


@auth_router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = await AuthService.user_exists(user.username, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username has already been taken")

    hashed_password = auth_handler.get_password_hash(user.password)
    created_user = await AuthService.create_user(
        username=user.username,
        password=hashed_password,
        email=user.email,
        db=db)
    return {"detail": "User has been registered successfully"}


@auth_router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    print(f"pass {user.password}")
    existing_user = await AuthService.user_exists(user.username, db)
    print(f"EX US {existing_user}")
    if (not existing_user) or (not auth_handler.verify_password(user.password, existing_user.password)):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(existing_user.id)
    return {'token': token}
