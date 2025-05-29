
from fastapi import FastAPI

app = FastAPI()

@app.get("/service1")
def read_root():
    return {"message": "Hello from Service 1!"}