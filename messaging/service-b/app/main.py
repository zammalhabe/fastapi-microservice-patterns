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


@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe("/from-service-a")


@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    await mqtt.publish("/from-service-b", f"{payload} forwarded by service-b")
