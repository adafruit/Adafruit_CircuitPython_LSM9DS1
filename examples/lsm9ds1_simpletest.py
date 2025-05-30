# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time

import board

import adafruit_lsm9ds1

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

# SPI connection:
# from digitalio import DigitalInOut, Direction
# spi = board.SPI()
# csag = DigitalInOut(board.D5)
# csag.direction = Direction.OUTPUT
# csag.value = True
# csm = DigitalInOut(board.D6)
# csm.direction = Direction.OUTPUT
# csm.value = True
# sensor = adafruit_lsm9ds1.LSM9DS1_SPI(spi, csag, csm)

# Main loop will read the acceleration, magnetometer, gyroscope, Temperature
# values every second and print them out.
while True:
    # Read acceleration, magnetometer, gyroscope, temperature.
    accel_x, accel_y, accel_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic
    gyro_x, gyro_y, gyro_z = sensor.gyro
    temp = sensor.temperature
    # Print values.
    print(f"Acceleration (m/s^2): ({accel_x:0.3f},{accel_y:0.3f},{accel_z:0.3f})")
    print(f"Magnetometer (gauss): ({mag_x:0.3f},{mag_y:0.3f},{mag_z:0.3f})")
    print(f"Gyroscope (rad/sec): ({gyro_x:0.3f},{gyro_y:0.3f},{gyro_z:0.3f})")
    print(f"Temperature: {temp:0.3f}C")
    # Delay for a second.
    time.sleep(1.0)
