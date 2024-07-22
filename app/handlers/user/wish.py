from contextlib import suppress

from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery

from app.filters import PrevWishCallback, PickWishCallback, NextWishCallback
from app.keyboards import InlineKeyboards
from app.utils import answer_wish_message, edit_wish_message
from data import Messages, Buttons
from database.services import WishManager, UserManager

wish_router = Router()


@wish_router.message(F.text == Buttons.START['pick_wish'])
async def __pick_wish(message: Message) -> None:
    wish_manager = WishManager()

    # Check for zero wishes
    if await wish_manager.count() == 0:
        await message.answer(Messages.ZERO_WISHES)
    else:
        index, wish = (await wish_manager.get_first_wish())
        keyboard = await InlineKeyboards.pick_wish(index, wish)
        await answer_wish_message(message, wish, keyboard)


@wish_router.callback_query(PrevWishCallback.filter())
async def __prev_wish(
        callback: CallbackQuery,
        callback_data: PrevWishCallback
) -> None:
    index = callback_data.index

    wish_manager = WishManager()
    index, wish = await wish_manager.get_prev_wish(index)
    keyboard = await InlineKeyboards.pick_wish(index, wish)
    await edit_wish_message(callback.message, wish, keyboard)


@wish_router.callback_query(NextWishCallback.filter())
async def __next_wish(
        callback: CallbackQuery,
        callback_data: NextWishCallback
) -> None:
    index = callback_data.index

    wish_manager = WishManager()
    index, wish = await wish_manager.get_next_wish(index)
    keyboard = await InlineKeyboards.pick_wish(index, wish)
    await edit_wish_message(callback.message, wish, keyboard)


@wish_router.callback_query(PickWishCallback.filter())
async def __pick_wish(
        callback: CallbackQuery,
        callback_data: PickWishCallback
) -> None:
    index = callback_data.index
    wish_id = callback_data.wish_id

    wish_manager = WishManager()
    user_manager = UserManager(callback.from_user.id)

    wish = await wish_manager.get_wish(wish_id)
    user = await user_manager.get_user()

    if wish.picked_user_id is None:
        wish.picked_user_id = user.id
        await wish_manager.update_picked_user_id(wish_id, user.id)
        await callback.answer(Messages.PICKED)
    elif wish.picked_user_id == user.id:
        wish.picked_user_id = None
        await callback.answer(Messages.PICK_CANCELED)
        await wish_manager.update_picked_user_id(wish_id, None)
    else:
        await callback.answer(Messages.ALREADY_PICKED)

    # Update keyboard
    keyboard = await InlineKeyboards.pick_wish(index, wish)
    with suppress(TelegramBadRequest):
        await callback.message.edit_reply_markup(reply_markup=keyboard)
