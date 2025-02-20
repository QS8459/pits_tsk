from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DATETIME
from pydantic import UUID4
from uuid import uuid4

from datetime import datetime


class Base(DeclarativeBase):
    uid: Mapped[UUID4] = mapped_column(default=uuid4, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow(), onupdate=datetime.utcnow())
    is_active: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.uid})>"

    def __str__(self):
        return f"<{self.__class__.__name__}(id={self.uid})>"
