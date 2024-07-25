from abc import ABC
from dataclasses import dataclass
from typing import Final

from .buttons import Buttons


@dataclass
class Messages(ABC):
    START: Final = ('🎀 Приветикс, {full_name}! 🎀\n\n'
                    'Тут ты можешь выбрать мне подарочек🥺\n\n\n'
                    '<b>Нажми на кнопочку <i>' + Buttons.START['pick_wish'] + '</i>\n'
                    'Листай подарочки стрелочками, и как увидишь тот, который '
                    'хочешь подарить, то жми на кнопочку ' + Buttons.PICK_WISH['unpicked'] + '\n'
                    'Тогда ты забронируешь его и все будут знать об этом</b>\n\n'
                    '<i>(Если у подарочка есть кнопка ' + Buttons.PICK_WISH['already_picked'] + ''
                    ', то его уже кто-то забронировал)</i>')
    START_PLACEHOLDER: Final = 'Подарочки, подарочки, подарочки...'

    ERROR: Final = 'Что-то пошло не так! 🤯'

    WISH_WITHOUT_CAPTION = 'Подписи неп 😅'

    SIMPLE_WISH = '<b>{caption}</b> - {href}'
    SIMPLE_WISH_WITHOUT_HREF = '<b>{caption}</b>'
    WISH: Final = '<b>🎀 {caption}</b>\n\n{href}'
    WISH_HREF: Final = '<a href="{link_url}"><b>Ссылочка</b></a>'

    PICKED: Final = 'Ура, ты забронировал подарочек 🥺'
    PICK_CANCELED: Final = 'Ой-ой, бронь отменена( 😢'
    ALREADY_PICKED: Final = 'Упс, эту штучку уже подарят 🥳'

    ZERO_WISHES: Final = 'Упс, подарочки еще не добавили 😣😣😣'

    MY_PICKED_WISHES_ZERO: Final = 'Ой-ой, ты не бронировал подарочки, скорее смотри и выбирай 🥰'
    MY_PICKED_WISHES_HEADER: Final = '🎀 Мои подарочки: 🎀\n'

    ABOUT = '🎀 <b>Written by @InDigitalE8 special for @tviiit and @tvitsay channel</b> 🎀'

    NOTIFY_NEW_WISHES = 'Привет! Я добавила новые подарочки, скорее проверяй 🥳'

    # Admin
    CANCEL_WISH: Final = 'Хорошо, подарочек не будем создавать! 😘'

    DELETE_WISH: Final = '<b>Подарочек удален из списка :( Лучшее впереди!🌟</b>'

    ADD_WISH_CAPTION: Final = 'Напиши название подарка, размер, цвет или другие уточнения, Настюш ✨'
    ADD_WISH_CAPTION_PLACEHOLDER = 'Описание подарочка...'

    ADD_WISH_LINK_URL: Final = 'Введи ссылку на подарок, зайчушка:'
    ADD_WISH_LINK_URL_PLACEHOLDER: Final = 'Ссылочка на подарочек...'

    ADD_WISH_PHOTO: Final = 'Отправь фото подарка, малыш:'
    ADD_WISH_PHOTO_PLACEHOLDER: Final = 'Фото подарочка...'

    ADD_WISH_DONE: Final = 'Подарочек успешно добавлен в список желаний! ✨'

    NOTIFY_SUCCESSFUL: Final = ('Уведомления отправлены, котёнок! 😘\n\n'
                                '<b>{users_count}</b> человек(а) получили твое сообщение')
