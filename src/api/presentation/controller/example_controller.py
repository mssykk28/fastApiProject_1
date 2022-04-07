from typing import List, NoReturn

from fastapi import APIRouter, HTTPException

from src.api.application.service import example_service
from src.api.presentation.schema import example_schema

router = APIRouter()


@router.get("/examples", tags=["examples"], response_model=List[example_schema.Example])
def get():  # noqa: ANN201
    """取得APIサンプル"""
    return example_service.find_all()


@router.post("/examples", tags=["examples"], status_code=201)
def post(payload: example_schema.ExampleCreate):  # noqa: ANN201
    """登録APIサンプル"""
    example_service.create(payload)
    return "登録成功"


@router.get("/examples/{example_id}", tags=["examples"])
def get_detail(example_id: int):  # noqa: ANN201
    """詳細取得APIサンプル"""
    _validation(example_id)
    return example_service.find_by_id(example_id)


@router.put("/examples/{example_id}", tags=["examples"], status_code=204)
def put(example_id: int, payload: example_schema.ExampleUpdate):  # noqa: ANN201
    """更新APIサンプル"""
    _validation(example_id)
    example_service.update(example_id, payload)
    return "更新成功"


@router.patch("/examples/{example_id}", tags=["examples"], status_code=204)
def patch(
    example_id: int, payload: example_schema.ExamplePortionUpdate
):  # noqa: ANN201
    """一部更新APIサンプル"""
    _validation(example_id)
    example_service.update(example_id, payload)
    return "更新成功"


@router.delete("/examples/{example_id}", tags=["examples"], status_code=204)
def delete(example_id: int):  # noqa: ANN201
    """削除APIサンプル"""
    _validation(example_id)
    example_service.delete(example_id)
    return "削除成功"


def _validation(example_id: int) -> NoReturn:
    example = example_service.find_by_id(example_id)
    if not example:
        raise HTTPException(status_code=404, detail=f"Example {example_id} not found")
