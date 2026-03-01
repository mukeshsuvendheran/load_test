import json
import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC
from excel_logger import log_data
from monitor import check_limits

def on_message(client, userdata, msg): # Callback function to handle incoming MQTT messages
    data = json.loads(msg.payload.decode()) # Decode JSON data from MQTT message
    print("Received:", data)  

    log_data(data)
    check_limits(data)

def start():
    client = mqtt.Client() # Create MQTT client instance
    client.connect(MQTT_BROKER, MQTT_PORT, 60) # Connect to MQTT broker
    client.subscribe(MQTT_TOPIC)
    client.on_message = on_message
    client.loop_forever()