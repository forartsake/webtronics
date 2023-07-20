
from src.app import App
from src.auth.router import auth_router
from src.posts.router import posts_router
from src.cache.router import cache_router

app = App(title="Webtronics",
              description='simple RESTful API using FastAPI for a social networking application')

app.include_router(auth_router)
app.include_router(posts_router)
app.include_router(cache_router)

