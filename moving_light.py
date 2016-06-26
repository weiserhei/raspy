# !/usr/bin/env python
# Author: weiserhei
# Lauflicht
# schaltet nacheinander angegebene Pins durch
# z.b. als LED Ampel

import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINS = [4, 17, 27]
count = 10
on_time = 0.2
off_time = 0.1

# Setup
for p in PINS:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.LOW)

try:
    # while count >=0 :
    while True:

        for p in PINS:
            GPIO.output(p, GPIO.HIGH)
            time.sleep(on_time)
            GPIO.output(p, GPIO.LOW)

            time.sleep(off_time)
            # count = count-1
except:
    print("")
    print("Exiting, cleaning up...")
    GPIO.cleanup()