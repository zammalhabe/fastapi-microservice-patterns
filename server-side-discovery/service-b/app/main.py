from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World from service-b"}


@app.get("/answer")
def ultimate_answer():
    return {"answer": 42}
