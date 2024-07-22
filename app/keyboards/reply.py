from abc import ABC
from dataclasses import dataclass
from typing import Final

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from data import Buttons, Messages


@dataclass
class ReplyKeyboards(ABC):
    START: Final = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=Buttons.START['pick_wish']),
                   KeyboardButton(text=Buttons.START['my_picked_wishes']),
                   KeyboardButton(text=Buttons.START['about'])
                   ]],
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=Messages.START_PLACEHOLDER
    )
    ADD_WISH_CAPTION: Final = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=Buttons.ADD_WISH['without_caption']),
                   KeyboardButton(text=Buttons.ADD_WISH['cancel'])]],
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=Messages.ADD_WISH_CAPTION_PLACEHOLDER
    )
    ADD_WISH_LINK_URL: Final = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=Buttons.ADD_WISH['without_link_url']),
                   KeyboardButton(text=Buttons.ADD_WISH['cancel'])]],
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=Messages.ADD_WISH_LINK_URL_PLACEHOLDER
    )
    ADD_WISH_PHOTO: Final = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=Buttons.ADD_WISH['without_photo']),
                   KeyboardButton(text=Buttons.ADD_WISH['cancel'])]],
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=Messages.ADD_WISH_PHOTO_PLACEHOLDER
    )
