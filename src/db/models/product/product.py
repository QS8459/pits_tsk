from src.db.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, INTEGER, DECIMAL, ForeignKey
from uuid import UUID

class Product(Base):
    __tablename__ = 'product'
    __table_args__ = {"schema": "public"}

    name: Mapped[str] = mapped_column(String(250), default=None, nullable=True)
    quantity: Mapped[int] = mapped_column(INTEGER, default=0, nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), default=0.0, nullable=False)
    category_uid: Mapped[UUID] = mapped_column(ForeignKey("public.category.uid"), nullable=False)

    category: Mapped["Cateogry"] = relationship("Category")


__all__ = "Product"