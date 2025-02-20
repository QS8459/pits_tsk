import re
from uuid import UUID
from pydantic import BaseModel, Field, AfterValidator
from typing_extensions import Annotated


def email_validation(email: str):
    try:
        if re.match(r'^[A-Za-z0-9]{6,20}@[A-Za-z0-9]+\.[A-z]{2,}$', email):
            return email
        else:
            raise ValueError('Email Validation Failed')
    except Exception as e:
        raise ValueError('Email failed')


def password_validation(pwd: str):
    try:
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z]).{5,}$', pwd):
            return pwd
        else:
            raise ValueError("PWD validation error")
    except Exception:
        raise ValueError('Pwd value error')


class AccountBaseSchema(BaseModel):
    email: Annotated[str, AfterValidator(email_validation)] = Field(
        default="example@email.domain",
        title="Email filed"
    )


class AccountAddSchema(AccountBaseSchema):
    password: Annotated[str, AfterValidator(password_validation)] = Field(
        default="pass",
        title="Password field"
    )


class AccountLoginSchema(AccountAddSchema):
    pass


class AccountResponseSchema(AccountBaseSchema):
    uid: UUID


class AccountGetSchema(BaseModel):
    access: str


class AccountEditSchema(AccountBaseSchema):
    pass