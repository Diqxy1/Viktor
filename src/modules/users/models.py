from typing import Optional
from pydantic import BaseModel, validator

from src.shared.validators import (
    DocValidator,
    EmailValidator,
    PhoneValidator
)


class UserModel(BaseModel):
    uuid: str
    name: str
    email: str
    is_active: Optional[bool]

    password: Optional[str]


    class Config:
        orm_mode = True


class CreateUserModel(BaseModel):
    name: str
    document: str
    email: str
    phone: str
    password: Optional[str]

    @validator('document')
    def document_validator(cls, v):
        assert DocValidator(v).cpf_validator(), 'Documento inválido'
        return v

    @validator('email')
    def email_validator(cls, v):
        assert EmailValidator(v).validate_email(), 'E-mail inválido'
        return v

    @validator('phone')
    def phone_validator(cls, v):
        assert PhoneValidator(v).validate_phone(), 'Telefone inválido'
        return v
