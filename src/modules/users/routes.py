from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

import requests

from src.config.database import get_database
from src.config.env import env

from src.modules.users.models import CreateUserModel, UserModel
from src.modules.users.services import (
    CreateUserService,
    DetailUserService,
    UpdateUserService,
    DeleteUserService
)



router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not Found'}}
)

@router.post('/', response_model=UserModel)
async def create_user(
    model: CreateUserModel,
    db: AsyncSession = Depends(get_database)
):
    service = CreateUserService(db)
    return await service.execute(model)

@router.get('/', response_model=UserModel)
async def detail_user(
    uuid: str = Query(),
    db: AsyncSession = Depends(get_database)
):
    service = DetailUserService(db)
    return await service.execute(uuid)

@router.put('/', response_model=UserModel)
async def update_user(
    update_model: CreateUserModel,
    uuid: str = Query(),
    db: AsyncSession = Depends(get_database)
):
    service = UpdateUserService(db)
    return await service.execute(uuid, update_model)

@router.delete('/', response_model=bool)
async def update_user(
    uuid: str = Query(),
    db: AsyncSession = Depends(get_database)
):
    service = DeleteUserService(db)
    return await service.execute(uuid)

@router.get('/get-location/')
async def get_location():
    my_ip = requests.get(env.get_item("URL", None))
    return my_ip.json()
