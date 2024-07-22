from typing import Tuple

from sqlalchemy import select, func

from database import Database
from database.models import Wish


class WishManager:
    def __init__(self) -> None:
        self._session_maker = Database().session_maker

    async def create_wish(self, caption: str, link_url: str, photo_id: str) -> Wish:
        wish = Wish(
            caption=caption,
            link_url=link_url,
            photo_id=photo_id
        )

        async with self._session_maker.begin() as session:
            session.add(wish)
            await session.commit()
        return wish

    async def delete_wish(self, wish_id: int) -> None:
        async with self._session_maker.begin() as session:
            wish = await session.get(Wish, wish_id)
            await session.delete(wish)
            await session.commit()

    async def update_picked_user_id(self, wish_id: int, picked_user_id: int | None):
        async with self._session_maker.begin() as session:
            wish = await session.get(Wish, wish_id)
            wish.picked_user_id = picked_user_id
            await session.commit()

    async def get_wish(self, wish_id: int) -> Wish | None:
        async with self._session_maker.begin() as session:
            return await session.get(Wish, wish_id)

    async def get_all_wishes(self):
        async with self._session_maker.begin() as session:
            statement = select(Wish)
            result = await session.execute(statement)
            return result.scalars().all()

    async def get_all_sort_wishes(self):
        # TODO: sort this
        return await self.get_all_wishes()

    async def get_all_user_picked_wishes(self, user_id: int):
        async with self._session_maker.begin() as session:
            statement = select(Wish).where(Wish.picked_user_id == user_id)
            result = await session.execute(statement)
            return result.scalars().all()

    async def count(self) -> int:
        async with self._session_maker.begin() as session:
            statement = select(func.count()).select_from(Wish)
            result = await session.execute(statement)
            return result.scalar()

    async def get_first_wish(self) -> Tuple[int, Wish]:
        wishes = await self.get_all_sort_wishes()
        return 0, wishes[0]

    async def get_next_wish(self, index: int) -> Tuple[int, Wish]:
        wishes = await self.get_all_sort_wishes()
        try:
            return index+1, wishes[index+1]
        except IndexError:
            return 0, wishes[0]

    async def get_prev_wish(self, index: int) -> Tuple[int, Wish]:
        wishes = await self.get_all_sort_wishes()
        try:
            return index-1, wishes[index-1]
        except IndexError:
            last = len(wishes)-1
            return last, wishes[last]
