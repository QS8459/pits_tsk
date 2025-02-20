from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class CategoryBaseSchema(BaseModel):
    title: str = Field(
        default="Parent",
        title="Category Name"
    )
    parent_uid: Optional[UUID | None | str] = Field(
        default=None,
        title="Parent category UUID"
    )


class CategoryAddUpdateSchema(CategoryBaseSchema):
    pass
    # parent_uid: Optional[str | None]


class CategoryResponseSchema(CategoryBaseSchema):
    uid: Optional[UUID]

