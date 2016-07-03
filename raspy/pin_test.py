# !/usr/bin/env python
# Author: weiserhei
# Test Pin Output, multiple Pins possible

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINS = [27]

for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

time.sleep(2)

for pin in PINS:
    GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()
