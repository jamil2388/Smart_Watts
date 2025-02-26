import paho.mqtt.client as mqtt
import json
from src.utils.db_handler import MongoDBHandler

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor_data"

db_handler = MongoDBHandler()

def on_message(client, userdata, msg):
    """Callback function triggered when a message is received."""
    data = json.loads(msg.payload.decode())
    db_handler.insert_data(data)
    print("Stored in DB:", data)

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("Listening for messages...")
client.loop_forever()
