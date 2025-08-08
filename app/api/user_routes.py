from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..core.database import get_db
from ..models.user import User
from ..repositories.user_repository import UserRepository

router = APIRouter()
user_repository = UserRepository()

@router.post("/users/", response_model=User)
async def create_user(user: User, db: AsyncSession = Depends(get_db)):
    return await user_repository.create_user(db, user)

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_repository.get_user(db, user_id)
