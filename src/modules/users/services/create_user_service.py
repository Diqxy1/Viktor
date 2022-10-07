from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.users.models import CreateUserModel, UserModel
from src.modules.users.repositories.user_repository import UserRepository


class CreateUserService:

    def __init__(self, db: AsyncSession):
        self._db = db
        self._repository = UserRepository(db)

    async def execute(self, create_user_model: CreateUserModel) -> UserModel:
        user = await self._create(create_user_model)
        return user

    async def _create(self, create_user_model: CreateUserModel) -> UserModel:
        user = await self._repository.create_user(create_user_model)
        return user
