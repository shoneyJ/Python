from typing import Union

from pydantic import BaseModel
from typing import TypeAlias
from database import Base

# Some generic types for the SQLAlchemy and Pydantic models
AppModel: TypeAlias = Base
AppSchema: TypeAlias = BaseModel

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []
    
    class Config:
        orm_mode = True



class BlogBase(BaseModel):
    title: str
    description: str
    category: str


class BlogCreate(BlogBase):
    pass


class Blog(BlogBase):
    id: int

    class Config:
        orm_mode = True