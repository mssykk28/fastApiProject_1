from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ExampleField:
    id = Field(
        title="id",
        description="id",
        example=1,
        min=1,
        max=4294967295,
    )

    example_string = Field(
        title="example_string",
        description="文字列サンプル",
        example="文字列サンプル",
        min_length=1,
        max_length=128,
        nullable=False,
    )

    example_number = Field(
        title="example_number",
        description="数値サンプル",
        example=1,
        min=1,
        max=4294967295,
        nullable=True,
    )

    example_datetime = Field(
        title="example_datetime",
        description="日時サンプル",
        example=datetime(2020, 1, 1, 0, 0, 0),
        nullable=True,
    )

    example_boolean = Field(
        title="example_boolean",
        description="真偽値サンプル",
        example=False,
        nullable=True,
    )


class Example(BaseModel):
    id: Optional[int] = ExampleField.id
    example_string: str = ExampleField.example_string
    example_number: Optional[int] = ExampleField.example_number
    example_datetime: Optional[datetime] = ExampleField.example_datetime
    example_boolean: Optional[bool] = ExampleField.example_boolean


class ExampleCreate(BaseModel):
    example_string: str = ExampleField.example_string
    example_number: int = ExampleField.example_number
    example_datetime: datetime = ExampleField.example_datetime
    example_boolean: bool = ExampleField.example_boolean


class ExampleUpdate(BaseModel):
    example_string: str = ExampleField.example_string
    example_number: int = ExampleField.example_number
    example_datetime: datetime = ExampleField.example_datetime
    example_boolean: bool = ExampleField.example_boolean


class ExamplePortionUpdate(BaseModel):
    example_string: Optional[str] = ExampleField.example_string
    example_number: Optional[int] = ExampleField.example_number
    example_datetime: Optional[datetime] = ExampleField.example_datetime
    example_boolean: Optional[bool] = ExampleField.example_boolean
