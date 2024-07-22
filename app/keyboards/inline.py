from abc import ABC
from dataclasses import dataclass

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.filters import DeleteWishCallback, PickWishCallback, PrevWishCallback, NextWishCallback
from data import Buttons
from database.models import Wish
from database.services import WishManager


@dataclass
class InlineKeyboards(ABC):
    @staticmethod
    def delete_wish(wish_id: int) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        builder.button(
            text=Buttons.DELETE_WISH['delete'],
            callback_data=DeleteWishCallback(wish_id=wish_id).pack()
        )
        builder.adjust(1)
        return builder.as_markup()

    @staticmethod
    async def pick_wish(index: int, wish: Wish) -> InlineKeyboardMarkup:
        wish_id = wish.id
        picked = True if wish.picked_user_id else False
        count = await WishManager().count()
        builder = InlineKeyboardBuilder()

        # Prev button
        if count >= 2:
            builder.button(
                text=Buttons.PICK_WISH['prev'],
                callback_data=PrevWishCallback(index=index).pack()
            )

        # Pick button
        builder.button(
            text=Buttons.PICK_WISH['already_picked'] if picked else Buttons.PICK_WISH['unpicked'],
            callback_data=PickWishCallback(index=index, wish_id=wish_id).pack()
        )

        # Next button
        if count >= 2:
            builder.button(
                text=Buttons.PICK_WISH['next'],
                callback_data=NextWishCallback(index=index).pack()
            )
        builder.adjust(3)
        return builder.as_markup()

