import json
import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

client = mqtt.Client() # Create MQTT client instance

def connect():
    client.connect(MQTT_BROKER, MQTT_PORT, 60) # Connect to MQTT broker

def publish_data(data):
    payload = json.dumps(data)  # Convert data to JSON string
    client.publish(MQTT_TOPIC, payload) # Publish data to MQTT topic