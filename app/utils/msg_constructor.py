from contextlib import suppress

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, InputMediaPhoto

from data import Messages
from database.models import Wish


def get_wish_message(wish: Wish) -> str:
    # Copy all data from wish
    caption: str = wish.caption
    link_url: str = wish.link_url

    # Prepare wish message
    href_message = Messages.WISH_HREF.format(
        link_url=link_url if link_url else ''
    )
    wish_message = Messages.WISH.format(
        caption=caption if caption else Messages.WISH_WITHOUT_CAPTION,
        href=href_message if link_url else ''
    )
    return wish_message


async def answer_wish_message(message: Message, wish: Wish, reply_markup=None) -> None:
    wish_message = get_wish_message(wish)
    photo_id: str = wish.photo_id

    await message.answer_photo(
        photo=photo_id,
        caption=wish_message,
        reply_markup=reply_markup
    )


async def edit_wish_message(message: Message, wish: Wish, reply_markup=None) -> None:
    wish_message = get_wish_message(wish)
    photo_id: str = wish.photo_id

    with suppress(TelegramBadRequest):
        await message.edit_media(
            media=InputMediaPhoto(
                media=photo_id,
                caption=wish_message,
            ),
            reply_markup=reply_markup
        )
