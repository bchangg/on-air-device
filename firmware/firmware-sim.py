import network
import time
from machine import Pin
import dht
import ujson
from umqtt.simple import MQTTClient
from dotenv import load_dotenv
import os
load_dotenv(Path(""))
redLed=Pin(13, Pin.OUT)

# MQTT Server Parameters
MQTT_CLIENT_ID = "siumulator-esp32"
MQTT_SERVER    = "5e390ad9ee8c4ed697aa80acc239403d.s2.eu.hivemq.cloud"
MQTT_PORT      = 0
MQTT_USER      = os.getenv('MQTT_USER')
MQTT_PASSWORD  = os.getenv('MQTT_PASSWORD')
MQTT_TOPIC     = "light-switch"
SSL_PARAMS     = {'server_hostname' : '5e390ad9ee8c4ed697aa80acc239403d.s2.eu.hivemq.cloud' }

# This connects to the wifi siumulation, replace this with the actual wifi credentials
print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

def mqtt_callback(topic, msg):
        if msg == b'on':
            redLed.value(1)
            print('topic received %s, message received %s lights on' % (topic, msg))
        elif msg == b'off': 
            redLed.value(0)
            print('topic received %s, message received %s lights off' % (topic msg))
        else:
            print((topic, msg))



print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, server=MQTT_SERVER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=7200, ssl=True, ssl_params=SSL_PARAMS)

client.connect()
client.set_callback(mqtt_callback)
client.subscribe(MQTT_TOPIC)
time.sleep(2)


print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_SERVER, MQTT_TOPIC))

while True:
    try:
       client.check_msg()
   

    except OSError as e:
        print ('Error %s' % (e))
