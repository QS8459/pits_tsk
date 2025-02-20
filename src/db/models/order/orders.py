'''
    What the hell is orders
'''

from src.db.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Order(Base):
    __tablename__ = "order"
    __table_args__ = {'schema': 'public'}

    title: Mapped[str] = mapped_column(String(350), nullable=True)

__all__ = "Order"