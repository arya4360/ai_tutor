import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class Settings:
    PROJECT_NAME:str = "AI Tutor"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432)
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","blogdb")
    DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    DATABASE_URL_ASYNC = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()