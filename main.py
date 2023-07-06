from fastapi import FastAPI
from src.auth.router import auth_router
from src.posts.router import posts_router

app = FastAPI(title="Webtronics",
              description='simple RESTful API using FastAPI for a social networking application')

app.include_router(auth_router)
app.include_router(posts_router)
