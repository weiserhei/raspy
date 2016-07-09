# !/usr/bin/env python
# Author: Thiele / http://tutorials-raspberrypi.de/raspberry-pi-luftfeuchtigkeit-temperatur-messen-dht11-dht22/
# DHT22 / AM2302 Temperature and Humidity Sensor

import Adafruit_DHT
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcd = Adafruit_CharLCD(rs=4, en=17,
                       d4=18, d5=22, d6=23, d7=24,
                       cols=16, lines=2)

lcd.set_cursor(0, 0)
lcd.clear()

sensor = Adafruit_DHT.DHT22
pin = 25


while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # print(humidity)
    # print(temperature)

    line1 = "Temp: " + str(temperature) + "*C"
    line2 = "Humidity: " + str(round(humidity, 2)) + "%"
    lcd.set_cursor(0, 0)
    lcd.message(line1)
    lcd.set_cursor(0, 1)
    lcd.message(line2)

    # 2 second cooldown on DHT22 minimum
    sleep(3)

GPIO.cleanup()
