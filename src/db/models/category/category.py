from src.db.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
from uuid import UUID


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {"schema": "public"}

    title: Mapped[str] = mapped_column(default=None, nullable=False, unique=True)
    parent_uid: Mapped[UUID] = mapped_column(ForeignKey("public.category.uid"),default=None, nullable=True)

    parent: Mapped["Category"] = relationship("Category",remote_side="Category.uid", back_populates="children")
    children: Mapped[List["Category"]] = relationship("Category",back_populates='parent', cascade='all, delete')


__all__ = "Category"
