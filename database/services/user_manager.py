from sqlalchemy import select

from database import Database
from database.models import User


class UserManager:
    def __init__(self, telegram_id: int) -> None:
        self._telegram_id = telegram_id
        self._session_maker = Database().session_maker

    async def create_user(self, check_exists: bool = True) -> User:
        if check_exists:
            user = await self.get_user()
            if user is not None:
                return user

        # create user
        user = User(telegram_id=self._telegram_id)
        async with self._session_maker.begin() as session:
            session.add(user)
            await session.commit()
        return user

    async def get_user(self) -> User | None:
        # find user by telegram id
        async with self._session_maker.begin() as session:
            statement = select(User).where(User.telegram_id == self._telegram_id)
            result = await session.execute(statement)
            user = result.scalar_one_or_none()

        # if the user is not found, then create it without checking for existence
        if user is None:
            return await self.create_user(check_exists=False)
        return user
