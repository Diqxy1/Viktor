from uuid import uuid4
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.users.entities.users import User
from src.modules.users.models import CreateUserModel, UserModel

class UserRepository:

    def __init__(self, db: AsyncSession):
        self._db = db

    async def create_user(self, model: CreateUserModel) -> UserModel:
        async with self._db:
            user = User(**model.dict())
            user.uuid = str(uuid4())
            user.code_reference = f"{model.document[3:]}{model.phone}"

            self._db.add(user)

            await self._db.commit()
            await self._db.refresh(user)

            return UserModel.from_orm(user) if user else None

    async def get_by_uuid(self, uuid: str) -> UserModel:
        async with self._db:
            user_entity = await self._db.execute(select(User).where(User.uuid == uuid))

            user = user_entity.scalar()

            return UserModel.from_orm(user) if user else None

    async def update_user(self, uuid: str, model: CreateUserModel) -> UserModel:
        async with self._db:
            user_entity = await self._db.execute(select(User).where(User.uuid == uuid))

            user = user_entity.scalar()

            user.name = model.name
            user.email = model.email
            user.password = model.password

            self._db.add(user)

            await self._db.commit()
            await self._db.refresh(user)

            return UserModel.from_orm(user) if user else None

    async def delete_user(self, uuid: str) -> bool:
        async with self._db:
            try:
                await self._db.execute(delete(User).where(User.uuid == uuid))

                await self._db.commit()

                return True
            except:
                return False

    async def get_by_email(self, email: str) -> UserModel:
        async with self._db:
            user_entity = await self._db.execute(select(User).where(User.email == email))

            user = user_entity.scalar()

            return UserModel.from_orm(user) if user else None

    async def get_by_phone(self, phone: str) -> UserModel:
        async with self._db:
            user_entity = await self._db.execute(select(User).where(User.phone == phone))

            user = user_entity.scalar()

            return UserModel.from_orm(user) if user else None

    async def get_by_document(self, document: str) -> UserModel:
        async with self._db:
            user_entity = await self._db.execute(select(User).where(User.document == document))

            user = user_entity.scalar()

            return UserModel.from_orm(user) if user else None
