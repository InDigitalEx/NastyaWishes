from sqlalchemy import String, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Wish(Base):
    __tablename__ = 'wish'

    id: Mapped[int] = mapped_column(primary_key=True)
    picked_user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id'), nullable=True)
    caption: Mapped[str] = mapped_column(String(1024), nullable=True)
    link_url: Mapped[str] = mapped_column(String(512), nullable=True)
    photo_id: Mapped[str] = mapped_column(String(128), nullable=True)
