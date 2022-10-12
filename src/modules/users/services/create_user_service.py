from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.users.models import CreateUserModel, UserModel
from src.modules.users.repositories.user_repository import UserRepository

from src.shared.services.password_generator_service import PasswordGeneratorService
from src.shared.exceptions.bad_exception import BadRequestException


class CreateUserService:

    def __init__(self, db: AsyncSession):
        self._db = db
        self._repository = UserRepository(db)
        self._password_generator = PasswordGeneratorService()

    async def execute(self, create_user_model: CreateUserModel) -> UserModel:
        # validations
        await self._make_validations(create_user_model)
        # create user
        user = await self._create(create_user_model)
        return user

    async def _create(self, create_user_model: CreateUserModel) -> UserModel:
        create_user_model.password = self._password_generator.generate(15)

        user = await self._repository.create_user(create_user_model)
        return user

    async def _make_validations(self, create_user_model: CreateUserModel):
        split_name = create_user_model.name.split(' ')

        if len(split_name) < 2:
            raise BadRequestException(message='Insira um sobrenome')

        if split_name[1] == '':
            raise BadRequestException(message='Insira um sobrenome valido')

        user_exist = await self._repository.get_by_document(create_user_model.document)

        if user_exist:
            raise BadRequestException(message='Cpf já cadastrado')

        email_exist = await self._repository.get_by_email(create_user_model.email)

        if email_exist:
            raise BadRequestException(message='E-mail já cadastrado')

        phone_exist = await self._repository.get_by_phone(create_user_model.phone)

        if phone_exist:
            raise BadRequestException(message='Telefone já cadastrado')

