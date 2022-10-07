from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.users.models import CreateUserModel, UserModel
from src.modules.users.repositories.user_repository import UserRepository

from src.shared.exceptions.bad_exception import BadRequestException


class UpdateUserService:

    def __init__(self, db: AsyncSession):
        self._db = db
        self._repository = UserRepository(db)

    async def execute(self, uuid: str, update_model: CreateUserModel) -> UserModel:
        user = await self._update(uuid, update_model)
        return user

    async def _update(self, uuid: str, update_model: CreateUserModel) -> UserModel:
        user = await self._repository.get_by_uuid(uuid)

        if not user:
            raise BadRequestException(message='User not found')

        update_user = await self._repository.update_user(user.uuid, update_model)

        return update_user
