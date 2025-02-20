from src.db.models.base import Base
from sqlalchemy import String, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from passlib.hash import pbkdf2_sha256 as sha256


class Account(Base):
    __tablename__ = "account"
    __table_args__ = {"schema": "public"}

    email: Mapped[String] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[String] = mapped_column(String, nullable=False)
    img_uid: Mapped[UUID] = mapped_column(ForeignKey("public.file.uid"), default=None, nullable=True)

    image: Mapped['File'] = relationship('File', foreign_keys=[img_uid])


    def hash_passwd(self, password):
        self.password = sha256.using().hash(password)

    def verify_passwd(self, password):
        return sha256.verify(password, self.password)


__all__ = ("Account")
