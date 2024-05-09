from ..models.user_model import UserModel

from sqlalchemy.ext.asyncio.session import async_session

class UserService:
    async def create_user(name):
        async with async_session() as session:
            session.add(UserModel(name=name))
            await session.commit()
