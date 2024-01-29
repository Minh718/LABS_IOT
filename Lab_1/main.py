import sys
from Adafruit_IO import MQTTClient
import random
import time 

AIO_FEED_ID = "sensor"
AIO_USERNAME = "minhprokute380"
AIO_KEY = "aio_CIET61ZGj67ye5cv0bgnrVCPaWEM"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
while True:
    counter = counter - 1
    if counter <= 0:
        counter = 10
        temp = random.randint(0, 100)
        client.publish("sensor", temp)
    time.sleep(1)
    pass