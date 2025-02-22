from fastapi import APIRouter, Depends, status, Form
from src.core.service.account.account import get_account_service
from src.core.service.account.authorization import (
    gen_jwt_token,
    get_user,
    refresh_token,
)
from src.core.schemas.account.account import (
    AccountAddSchema,
    AccountResponseSchema,
    AccountLoginSchema,
    AccountGetSchema,
    AccountEditSchema,
)
from src.core.schemas.account.auth import TokenResponseModel, TokenRefreshBodySchema
from src.conf.log import log

account_api: APIRouter = APIRouter(prefix="/account", tags=["Account"])


@account_api.post(
    "/registration/",
    status_code=status.HTTP_201_CREATED,
    response_model=AccountResponseSchema,
)
async def add_account(data: AccountAddSchema, service=Depends(get_account_service)):
    return await service.add(**data.dict())


@account_api.post(
    "/authorization/",
    status_code=status.HTTP_200_OK,  # , response_model=TokenResponseModel
)
async def login(
    username: str = Form(...),
    password: str = Form(...),
    service=Depends(get_account_service),
):
    user_data: dict = {"email": username, "password": password}
    user = await service.verify_user(**user_data)
    user_data.update({"uid": str(user.uid)})
    if user:
        return gen_jwt_token(data=user_data)


@account_api.post(
    "/me/", status_code=status.HTTP_200_OK, response_model=AccountResponseSchema
)
async def me(
    data: AccountGetSchema = Depends(get_user), service=Depends(get_account_service)
):
    if data:
        return await service.get_by_email(email=data.get("email"))


@account_api.post(
    "/refresh/", status_code=status.HTTP_200_OK, response_model=TokenResponseModel
)
async def refresh(
    data: TokenRefreshBodySchema,
):
    return refresh_token(token=data.dict().get("access"))


@account_api.get(
    "/{pk}/", status_code=status.HTTP_200_OK, response_model=AccountResponseSchema
)
async def account_by_id(pk: str, service=Depends(get_account_service)):
    return await service.get_by_id(uid=pk)


@account_api.put(
    "/edit/{pk}/",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=AccountResponseSchema,
)
async def edit_account_data(
    pk: str, data: AccountEditSchema, service=Depends(get_account_service)
):
    return await service.update(uid=pk, **data.dict())


@account_api.delete("/delete/{pk/", status_code=status.HTTP_202_ACCEPTED)
async def delete_account(pk: str, service=Depends(get_account_service)):
    return await service.h_delete(uid=pk)
