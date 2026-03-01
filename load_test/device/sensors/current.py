# import random

# def read_current():
#     return round(random.uniform(8, 15), 2)





sensor_voltage = chan.voltage

zero_offset = 2.5
sensitivity = 0.1

current = (sensor_voltage - zero_offset) / sensitivity
print("DC Current:", current, "A")