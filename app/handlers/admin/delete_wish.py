from aiogram import Router
from aiogram.exceptions import AiogramError
from aiogram.types import CallbackQuery
from sqlalchemy.exc import SQLAlchemyError

from app.filters import DeleteWishCallback, IsAdmin
from data import Messages
from database.services import WishManager

delete_wish_router = Router()


@delete_wish_router.callback_query(DeleteWishCallback.filter(), IsAdmin())
async def __delete_wish_callback(
        callback: CallbackQuery,
        callback_data: DeleteWishCallback
) -> None:
    try:
        await WishManager().delete_wish(callback_data.wish_id)
        await callback.message.answer(Messages.DELETE_WISH)
        await callback.message.delete()
    except (AiogramError, SQLAlchemyError):
        await callback.answer(Messages.ERROR)
