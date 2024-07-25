from contextlib import suppress

from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.types import Message

from app.filters import IsAdmin
from data import Messages
from database.services import UserManager

notify_router = Router()


@notify_router.message(Command('notify'), IsAdmin())
async def __notify_new_wishes(message: Message):
    user_manager = UserManager(message.from_user.id)
    users = await user_manager.get_all_users()

    counter = 0
    for user in users:
        if user.telegram_id == message.from_user.id:
            continue
        with suppress(TelegramBadRequest):
            success = await message.bot.send_message(
                user.telegram_id, Messages.NOTIFY_NEW_WISHES)
            if success:
                counter += 1

    # Send successful message to user
    await message.answer(Messages.NOTIFY_SUCCESSFUL.format(users_count=counter))
