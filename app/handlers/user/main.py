from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters import StateFilter
from aiogram.types import Message

from app.keyboards.reply import ReplyKeyboards
from data import Messages, Buttons
from database.services import UserManager, WishManager
from .wish import wish_router

user_router = Router()


@user_router.startup()
async def __user_router_startup(router: Router) -> None:
    router.include_routers(
        wish_router,
    )


@user_router.message(StateFilter(None), CommandStart())
async def __start_message(message: Message) -> None:
    user_manager = UserManager(message.from_user.id)
    await user_manager.create_user()

    await message.answer(Messages.START.format(
        full_name=message.from_user.full_name),
        reply_markup=ReplyKeyboards.START
    )


@user_router.message(StateFilter(None), F.text == Buttons.START['my_picked_wishes'])
async def __my_picked_wishes(message: Message) -> None:
    user_manager = UserManager(message.from_user.id)
    wish_manager = WishManager()
    user = await user_manager.get_user()
    wishes = await wish_manager.get_all_user_picked_wishes(user.id)

    if len(wishes) == 0:
        await message.answer(
            Messages.MY_PICKED_WISHES_ZERO,
            reply_markup=ReplyKeyboards.START
        )
    else:
        text = Messages.MY_PICKED_WISHES_HEADER
        for index, wish in enumerate(wishes, start=1):
            caption = wish.caption if wish.caption != '' else Messages.WISH_WITHOUT_CAPTION

            if wish.link_url == '':
                text += f'\n{index}. ' + Messages.SIMPLE_WISH_WITHOUT_HREF.format(
                    caption=caption
                )
            else:
                href = Messages.WISH_HREF.format(link_url=wish.link_url)
                text += f'\n{index}. ' + Messages.SIMPLE_WISH.format(
                    caption=caption,
                    href=href
                )
        await message.answer(text, reply_markup=ReplyKeyboards.START)


@user_router.message(StateFilter(None), F.text == Buttons.START['about'])
async def __about(message: Message) -> None:
    await message.answer(Messages.ABOUT, reply_markup=ReplyKeyboards.START)
