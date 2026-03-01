# import random

# def read_rpm():
#     # Replace with real sensor logic
#     return random.randint(1400, 1600)



#LM393 → hall effect sensor connected to Raspberry Pi
import RPi.GPIO as GPIO
import time

sensor = 17
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

def count_pulse(channel):
    global count
    count += 1

GPIO.add_event_detect(sensor, GPIO.RISING, callback=count_pulse)

while True:
    count = 0
    time.sleep(1)
    rpm = count * 60
    print("RPM:", rpm)