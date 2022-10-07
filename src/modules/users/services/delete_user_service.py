from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.users.repositories.user_repository import UserRepository

from src.shared.exceptions.bad_exception import BadRequestException


class DeleteUserService:

    def __init__(self, db: AsyncSession):
        self._db = db
        self._repository = UserRepository(db)

    async def execute(self, uuid: str) -> bool:
        user = await self._delete(uuid)
        return user

    async def _delete(self, uuid: str) -> bool:
        user = await self._repository.get_by_uuid(uuid)

        if not user:
            raise BadRequestException(message='User not found')

        update_user = await self._repository.delete_user(user.uuid)

        return update_user
