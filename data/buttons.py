from abc import ABC
from dataclasses import dataclass


@dataclass
class Buttons(ABC):
    START = {
        'pick_wish': 'Выбрать подарочек 🎁',
        'my_picked_wishes': 'Мои подарочки 🥺',
        'about': 'О ботике 👨‍💻'
    }
    ADD_WISH = {
        'cancel': '❌',
        'without_caption': 'Без подписи 😌',
        'without_link_url': 'Без ссылочки 🤓',
        'without_photo': 'Без фоточки 😏'
    }
    DELETE_WISH = {
        'delete': '🗑'
    }
    PICK_WISH = {
        'already_picked': '❌',
        'unpicked': '✅',
        'prev': '◀️',
        'next': '▶️'
    }
