from src.db.models.base import Base
from sqlalchemy import String, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class File(Base):
    __tablename__ = 'file'
    __table_args__ = {"schema": 'public'}

    title: Mapped[String] = mapped_column(String(250), nullable=False)
    path: Mapped[String] = mapped_column(String(1000), nullable=False)
    type: Mapped[String] = mapped_column(String(10), nullable=False)
    owner: Mapped[UUID] = mapped_column(ForeignKey('public.account.uid'), nullable=True)

    account: Mapped['Account'] = relationship('Account', foreign_keys=[owner])


__all__ = "File"