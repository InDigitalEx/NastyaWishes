from aiogram.filters import Filter
from aiogram.types import Message

from database.services import UserManager


class IsAdmin(Filter):
    async def __call__(self, message: Message) -> bool:
        user_manager = UserManager(message.from_user.id)
        user = await user_manager.get_user()
        return user.is_admin
