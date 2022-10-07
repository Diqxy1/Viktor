from typing import Optional
from pydantic import BaseModel


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
    email: str
    password: str
