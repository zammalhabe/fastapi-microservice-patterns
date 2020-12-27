from fastapi import FastAPI

from starlette_prometheus import metrics, PrometheusMiddleware


app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", metrics)


@app.get("/")
def read_root():
    return {"Hello": "World"}
