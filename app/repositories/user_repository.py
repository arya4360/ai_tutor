from sqlalchemy.ext.asyncio import AsyncSession
from ..models.database_models import UserDB
from ..models.user import User
from ..core.logging import logger

class UserRepository:
    async def create_user(self, db: AsyncSession, user: User):
        db_user = UserDB(**user.dict())
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        logger.info(f"User created: {db_user.id}")
        return db_user

    async def get_user(self, db: AsyncSession, user_id: int):
        result = await db.get(UserDB, user_id)
        return result
