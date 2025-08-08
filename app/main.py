from typing import Union
from fastapi import FastAPI
from app.core.logging import logger
from app.core.database import init_db
from app.api.user_routes import router as user_router

app = FastAPI()

# Include routers
app.include_router(user_router, tags=["users"])

@app.on_event("startup")
async def startup_event():
    logger.info("Initializing database")
    await init_db()
    logger.info("Database initialized")

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}