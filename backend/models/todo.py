from typing import Optional
from pydantic import BaseModel

from .dbmodel import DateTimeModelMixin, DBModelMixin


class TodoBase(BaseModel):
    title: str


class Todo(TodoBase):
    pass


class TodoInDB(DBModelMixin, Todo):
    pass
