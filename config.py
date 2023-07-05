from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DATABASE_HOST')
DB_NAME = os.getenv('POSTGRES_DB')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
DB_PORT = os.getenv('DATABASE_PORT')
DB_USER = os.getenv('DATABASE_USER')
AUTH_KEY = os.getenv('AUTH_SECRET_KEY')
AUTH_ALGORITHM = os.getenv('ALGORITHM')
AUTH_ACCESS_TOKEN_EXPIRE_TIME = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')