from aiogram import Router

from .add_wish import add_wish_router
from .delete_wish import delete_wish_router

admin_router = Router()


@admin_router.startup()
async def __admin_router_startup(router: Router) -> None:
    router.include_routers(
        add_wish_router,
        delete_wish_router
    )
