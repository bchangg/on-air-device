import time

import config
import network
from machine import Pin
from umqtt.simple import MQTTClient

redLed = Pin(13, Pin.OUT)

# MQTT Server Parameters
MQTT_CLIENT_ID = config.MQTT_CLIENT_ID
MQTT_SERVER = config.MQTT_SERVER
MQTT_PORT = config.MQTT_PORT
MQTT_USER = config.MQTT_USER
MQTT_PASSWORD = config.MQTT_PASSWORD
MQTT_TOPIC = config.MQTT_TOPIC
SSL_PARAMS = config.SSL_PARAMS


client = MQTTClient(
    client_id=MQTT_CLIENT_ID,
    server=MQTT_SERVER,
    port=MQTT_PORT,
    user=MQTT_USER,
    password=MQTT_PASSWORD,
    keepalive=7200,
    ssl=True,
    ssl_params=SSL_PARAMS,
)


def mqtt_callback(topic, msg):
    if msg == b"on":
        redLed.value(1)
        print("topic received %s, message received %s lights on" % (topic, msg))
    elif msg == b"off":
        redLed.value(0)
        print("topic received %s, message received %s lights off" % (topic, msg))
    else:
        print((topic, msg))


def connect_and_subscribe():
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print(
        "Connected to %s MQTT broker, subscribed to %s topic"
        % (MQTT_SERVER, MQTT_TOPIC)
    )


try:
    connect_and_subscribe()
except OSError as e:
    print(e)

while True:
    try:
        client.check_msg()

    except OSError as e:
        print("Error %s" % (e))
