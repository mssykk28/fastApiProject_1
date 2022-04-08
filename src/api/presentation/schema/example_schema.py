from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Example(BaseModel):
    id: Optional[int]
    example_string: str
    example_number: Optional[int]
    example_datetime: Optional[datetime]
    example_boolean: Optional[bool]


class ExampleCreate(BaseModel):
    example_string: str
    example_number: int
    example_datetime: datetime
    example_boolean: bool


class ExampleUpdate(BaseModel):
    example_string: str
    example_number: int
    example_datetime: datetime
    example_boolean: bool


class ExamplePortionUpdate(BaseModel):
    example_string: Optional[str]
    example_number: Optional[int]
    example_datetime: Optional[datetime]
    example_boolean: Optional[bool]
