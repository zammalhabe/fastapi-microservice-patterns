from typing import Optional

from fastapi import FastAPI

import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World from service-a"}

@app.get("/ask")
def request_answer():
    endpoint_of_service_b = "http://service-b/answer"
    response_of_service_b = requests.get(endpoint_of_service_b)
    json_response_of_service_b = response_of_service_b.json()
    return {"answer via service-b": json_response_of_service_b["answer"]}

