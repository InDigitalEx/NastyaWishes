from aiogram.fsm.state import State, StatesGroup


class AddWish(StatesGroup):
    caption = State()
    link_url = State()
    photo = State()
