from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.filters import IsAdmin
from app.keyboards import ReplyKeyboards, InlineKeyboards
from app.states import AddWish
from app.utils import answer_wish_message
from data import Buttons, Messages, config
from database.services import WishManager

add_wish_router = Router()


# Cancel
@add_wish_router.message(
    StateFilter(AddWish),
    F.text == Buttons.ADD_WISH['cancel'],
    IsAdmin()
)
@add_wish_router.message(StateFilter(AddWish), Command('cancel'), IsAdmin())
async def __cancel(message: Message, state: FSMContext) -> None:
    await message.answer(Messages.CANCEL_WISH, reply_markup=ReplyKeyboards.START)
    await state.clear()


# /add_wish
@add_wish_router.message(StateFilter(None), Command('add'), IsAdmin())
async def add_wish(message: Message, state: FSMContext) -> None:
    await message.answer(Messages.ADD_WISH_CAPTION, reply_markup=ReplyKeyboards.ADD_WISH_CAPTION)
    await state.set_state(AddWish.caption)


# Add caption
@add_wish_router.message(StateFilter(AddWish.caption), F.text, IsAdmin())
async def add_wish_caption(message: Message, state: FSMContext) -> None:
    if message.text == Buttons.ADD_WISH['without_caption']:
        await state.update_data(caption='')
    else:
        await state.update_data(caption=message.text)

    await message.answer(Messages.ADD_WISH_LINK_URL, reply_markup=ReplyKeyboards.ADD_WISH_LINK_URL)
    await state.set_state(AddWish.link_url)


# Add link url
@add_wish_router.message(StateFilter(AddWish.link_url), F.text, IsAdmin())
async def add_wish_link_url(message: Message, state: FSMContext) -> None:
    if message.text == Buttons.ADD_WISH['without_link_url']:
        await state.update_data(link_url='')
    else:
        await state.update_data(link_url=message.text)

    await message.answer(Messages.ADD_WISH_PHOTO, reply_markup=ReplyKeyboards.ADD_WISH_PHOTO)
    await state.set_state(AddWish.photo)


# Add photo
@add_wish_router.message(
    StateFilter(AddWish.photo),
    F.text == Buttons.ADD_WISH['without_photo'],
    IsAdmin()
)
@add_wish_router.message(StateFilter(AddWish.photo), F.photo, IsAdmin())
async def add_wish_photo(message: Message, state: FSMContext) -> None:
    if message.text == Buttons.ADD_WISH['without_photo']:
        await state.update_data(photo_id=config.default_photo)
    else:
        await state.update_data(photo_id=message.photo[-1].file_id)

    # Parse data from state
    data = await state.get_data()

    # Create wish in database
    wish_manager = WishManager()
    wish = await wish_manager.create_wish(data['caption'], data['link_url'], data['photo_id'])

    # Send message
    await message.answer(Messages.ADD_WISH_DONE, reply_markup=ReplyKeyboards.START)
    await answer_wish_message(message, wish, InlineKeyboards.delete_wish(wish.id))

    # Clear state
    await state.clear()
