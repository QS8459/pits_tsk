from pydantic import BaseModel


class TokenBaseSchema(BaseModel):
    access: str


class TokenResponseModel(TokenBaseSchema):
    refresh: str


class TokenRefreshBodySchema(TokenBaseSchema):
    pass
