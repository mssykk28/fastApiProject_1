from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/hello/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/hello")
async def create_item(item: Item):
    return item


@app.put("/hello/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id}


@app.delete("/hello/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id}
