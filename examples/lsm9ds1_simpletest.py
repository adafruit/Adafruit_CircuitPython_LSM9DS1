# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time

import board
import busio
# import digitalio # Use when connected over SPI

import adafruit_lsm9ds1


# You have a couple options for wiring this sensor, either I2C (recommended)
# or a SPI connection.  Choose _one_ option below and uncomment it:

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

# SPI connection:
#spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
#xgcs = digitalio.DigitalInOut(board.D5)  # Pin connected to XGCS (accel/gyro chip select).
#mcs  = digitalio.DigitalInOut(board.D6)  # Pin connected to MCS (magnetometer chip select).
#sensor = adafruit_lsm9ds1.LSM9DS1_SPI(spi, xgcs, mcs)

# Main loop will read the acceleration, magnetometer, gyroscope, Temperature
# values every second and print them out.
while True:
    # Read acceleration, magnetometer, gyroscope, temperature.
    accel_x, accel_y, accel_z = sensor.accelerometer
    mag_x, mag_y, mag_z = sensor.magnetometer
    gyro_x, gyro_y, gyro_z = sensor.gyroscope
    temp = sensor.temperature
    # Print values.
    print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(accel_x, accel_y, accel_z))
    print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(mag_x, mag_y, mag_z))
    print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
    print('Temperature: {0:0.3f}C'.format(temp))
    # Delay for a second.
    time.sleep(1.0)
