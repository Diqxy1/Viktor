from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.users.models import UserModel
from src.modules.users.repositories.user_repository import UserRepository

from src.shared.exceptions.bad_exception import BadRequestException


class DetailUserService:

    def __init__(self, db: AsyncSession):
        self._db = db
        self._repository = UserRepository(db)

    async def execute(self, uuid: str) -> UserModel:
        user = await self._detail(uuid)
        return user

    async def _detail(self, uuid: str) -> UserModel:
        user = await self._repository.get_by_uuid(uuid)

        if not user:
            raise BadRequestException(message='User not found')

        return user
