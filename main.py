from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Docker FastAPI example!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}


