import sys
from Adafruit_IO import MQTTClient
import random
import time 

AIO_FEED_ID = "sensor"
AIO_USERNAME = "minhprokute380"
AIO_KEY = "aio_TMot68LNAMjqZL8d17Sbyl56MuJc"

def connected(client):
    print("Connected to Adafruit IO! Listening for feed changes...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to feed with ID: {}".format(AIO_FEED_ID))

def disconnected(client):
    print("Disconnected from Adafruit IO!")
    sys.exit(1)

def message(client, feed_id, payload):
    print("Received data from feed {}: {}".format(feed_id, payload))

client = MQTTClient(AIO_USERNAME, AIO_KEY)

# Assign callback functions
client.on_connect = connected
client.on_subscribe = subscribe
client.on_disconnect = disconnected
client.on_message = message

# Connect to Adafruit IO
client.connect()

# Loop forever listening for changes to the specified feeds
client.loop_blocking()
