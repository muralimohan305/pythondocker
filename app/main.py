from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    available: bool = True

items = {
    1: {"name": "Sample Item", "description": "A demo item", "price": 9.99, "available": True}
}

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI with Docker!"}

@app.get("/health")
async def healthcheck():
    return {"status": "ok"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items")
async def create_item(item: Item):
    next_id = max(items.keys(), default=0) + 1
    items[next_id] = item.dict()
    return {"id": next_id, **items[next_id]}
