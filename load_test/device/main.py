import time
from datetime import datetime
from sensors.rpm import read_rpm
from sensors.voltage import read_voltage
from sensors.current import read_current
from sensors.temperature import read_temperature
from publisher import connect, publish_data
from config import PUBLISH_INTERVAL

connect()

while True:
    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rpm": read_rpm(),
        "voltage": read_voltage(),
        "current": read_current(),
        "temperature": read_temperature()
    }

    publish_data(data)
    print("Published:", data)
    time.sleep(PUBLISH_INTERVAL)