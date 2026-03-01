# import random

# def read_temperature():
#     return round(random.uniform(70, 115), 2)



#MLX90614 → Raspberry Pi
import time
import board
import busio
import adafruit_mlx90614

# I2C Setup
i2c = busio.I2C(board.SCL, board.SDA)
mlx = adafruit_mlx90614.MLX90614(i2c)

while True:
    ambient_temp = mlx.ambient_temperature
    object_temp = mlx.object_temperature

    print("Ambient Temp: {:.2f} °C".format(ambient_temp))
    print("Motor Surface Temp: {:.2f} °C".format(object_temp))
    print("-----------------------------")

    time.sleep(2)