from aiogram.filters.callback_data import CallbackData


class DeleteWishCallback(CallbackData, prefix='delete_wish'):
    wish_id: int


class PickWishCallback(CallbackData, prefix='pick_wish'):
    index: int
    wish_id: int


class PrevWishCallback(CallbackData, prefix='prev_wish'):
    index: int


class NextWishCallback(CallbackData, prefix='next_wish'):
    index: int
