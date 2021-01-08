from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    string_to_display: str = "World"


settings = Settings()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": settings.string_to_display}
