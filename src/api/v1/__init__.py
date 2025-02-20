from fastapi import APIRouter
from src.api.v1.category import category_api
from src.api.v1.product import product_api
from src.api.v1.account.account import account_api
from src.api.v1.file import file_api

v1: APIRouter= APIRouter(prefix='/v1')

v1.include_router(category_api)
v1.include_router(product_api)
v1.include_router(account_api)
v1.include_router(file_api)