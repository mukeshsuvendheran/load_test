# import random

# def read_voltage():
#     return round(random.uniform(48, 54), 2)


#ADS1115 → voltage sensor connected to Raspberry Pi
import time
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

chan = AnalogIn(ads, ADS1115.P0)

while True:
    voltage = chan.voltage
    print("DC Voltage:", voltage)
    time.sleep(1)
