from fastapi import APIRouter, HTTPException

from ..services.user_service import UserService


user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')


@user_router.post('/create')
async def user_create(user_input):
    try:
        await UserService.create_user(name=user_input.name)
        return "ok"
    except Exception as error:
        raise HTTPException(400, detail=str(error))