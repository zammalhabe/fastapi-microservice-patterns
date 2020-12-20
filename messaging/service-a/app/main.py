from typing import Optional

from fastapi import FastAPI

from fastapi_mqtt import FastMQTT, MQQTConfig


app = FastAPI()

mqtt_config = MQQTConfig(host = "mqtt-broker")

mqtt = FastMQTT(
    config=mqtt_config
)


@app.on_event("startup")
async def startup():
    await mqtt.connection()


@app.on_event("shutdown")
async def shutdown():
    await mqtt.client.disconnect()


@app.post("/send/{payload}")
async def request_answer(payload: str):
    await mqtt.publish("/from-service-a", payload)
