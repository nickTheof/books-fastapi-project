from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=3, max_length=100)
    description: str = Field(max_length=1000, default='')
    rating: int = Field(ge=1, le=5)


class BookCreate(BookBase):
    pass 


class BookUpdate(BaseModel):
    description: str = Field(max_length=1000, default='')
    rating: int = Field(ge=1, le=5)


class BookRead(BookBase):
    id: int


class Book(BookRead):
    pass 


Book.model_config = {'from_attributes': True}