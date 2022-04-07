from typing import NoReturn, Optional, Union

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.api.presentation.schema.example_schema import (
    ExampleCreate,
    ExamplePortionUpdate,
    ExampleUpdate,
)
from src.infrastructure.db.connection import db_connection
from src.infrastructure.db.entity.example import Example
from src.infrastructure.db.repository import example_repository


@db_connection()
def find_all(db_session: Session) -> JSONResponse:
    examples = example_repository.find_all(db_session)
    return JSONResponse(content=jsonable_encoder(examples))


@db_connection()
def create(payload: ExampleCreate, db_session: Session) -> NoReturn:
    example_repository.create(db_session, Example(**payload.dict()))


@db_connection()
def find_by_id(example_id: int, db_session: Session) -> Optional[JSONResponse]:
    example = example_repository.find_by_id(db_session, example_id)
    if not example:
        return None

    return JSONResponse(content=jsonable_encoder(example))


@db_connection()
def update(
    example_id: int,
    example_model: Union[ExampleUpdate, ExamplePortionUpdate],
    db_session: Session,
) -> NoReturn:
    example_repository.update(db_session, example_id, Example(**example_model.dict()))


@db_connection()
def delete(example_id: int, db_session: Session) -> NoReturn:
    example_repository.delete(db_session, example_id)
