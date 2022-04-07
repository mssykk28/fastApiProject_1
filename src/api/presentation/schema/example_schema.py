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


# id = Integer(
#     title="id",
#     description="id",
#     required=False,
#     example=1,
#     min=1,
#     max=4294967295,
#     readonly=True,
# )
#
# example_string = String(
#     title="example_string",
#     description="文字列サンプル",
#     required=True,
#     example="文字列サンプル",
#     min_length=1,
#     max_length=128,
#     nullable=False,
# )
#
# example_number = Integer(
#     title="example_number",
#     description="数値サンプル",
#     required=True,
#     example=123,
#     min=1,
#     max=4294967295,
#     nullable=True,
# )
#
# example_datetime = DateTime(
#     title="example_datetime",
#     description="日時サンプル",
#     required=True,
#     example="2022-03-01T08:09:10",
#     nullable=True,
# )
#
# example_boolean = Boolean(
#     title="example_boolean",
#     description="真偽値サンプル",
#     required=True,
#     example=False,
#     nullable=True,
# )
#
# def example_get_response_model(self) -> dict:
#     return self.api.model(
#         "ExampleGetResponse",
#         {
#             "id": self.id,
#             "example_string": self.example_string,
#             "example_number": self.example_number,
#             "example_datetime": self.example_datetime,
#             "example_boolean": self.example_boolean,
#         },
#     )
#
# def example_post_request_model(self) -> dict:
#     return self.api.model(
#         "ExamplePostRequest",
#         {
#             "example_string": self.example_string,
#             "example_number": self.example_number,
#             "example_datetime": self.example_datetime,
#             "example_boolean": self.example_boolean,
#         },
#     )
#
# def example_put_request_model(self) -> dict:
#     return self.api.model(
#         "ExamplePutRequest",
#         {
#             "example_string": self.example_string,
#             "example_number": self.example_number,
#             "example_datetime": self.example_datetime,
#             "example_boolean": self.example_boolean,
#         },
#     )
#
# def example_patch_request_model(self) -> dict:
#     _example_string = deepcopy(self.example_string)
#     _example_string.required = False
#
#     _example_number = deepcopy(self.example_number)
#     _example_number.required = False
#
#     _example_datetime = deepcopy(self.example_datetime)
#     _example_datetime.required = False
#
#     _example_boolean = deepcopy(self.example_boolean)
#     _example_boolean.required = False
#
#     return self.api.model(
#         "ExamplePatchRequest",
#         {
#             "example_string": _example_string,
#             "example_number": _example_number,
#             "example_datetime": _example_datetime,
#             "example_boolean": _example_boolean,
#         },
#     )
