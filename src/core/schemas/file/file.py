from pydantic import BaseModel
from uuid import UUID


class FileBaseSchema(BaseModel):
    uid: UUID
    title: str
    type: str | None


class FileResponseSchema(FileBaseSchema):
    pass
