import time
import paho.mqtt.client as mqtt
import json
from src.iot.ac import AC
from src.iot.refrigerator import Refrigerator

BROKER = "localhost"  # Use your MQTT broker address
PORT = 1883
TOPIC = "iot/sensor_data"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

devices = [AC(), Refrigerator()]

while True:
    for device in devices:
        data = device.get_data()
        json_data = json.dumps(data)
        client.publish(TOPIC, json_data)
        print("Published:", json_data)
    time.sleep(2)
