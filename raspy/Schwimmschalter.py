# !/usr/bin/env python
# Author: http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
# Test Callback and Interrupt
# IMPORTANT! BUTTON1 must be connected to 3.3V Source

from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcd = Adafruit_CharLCD(rs=4, en=17,
                       d4=18, d5=22, d6=23, d7=24,
                       cols=16, lines=2)

lcd.set_cursor(0, 0)
BUTTON1 = 21
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def printFunction(channel):

    state = GPIO.input(channel)
    lcd.clear()
    print("callback")
    if state is 1:
        message = "Im so wet"
    else:
        message = "Bin so durstig"

    lcd.message(message)

    return

# GPIO.add_event_detect(BUTTON1, GPIO.RISING, callback=printFunction, bouncetime=300)
GPIO.add_event_detect(BUTTON1, GPIO.BOTH, callback=printFunction, bouncetime=100)


# while 1:
#
#     sleep(2)

while True:

    sleep(1)

GPIO.cleanup()
