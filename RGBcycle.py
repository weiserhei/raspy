# !/usr/bin/env python
# Author http://crazyice.net/?p=164
# Cycle RGB LED Colors (red, violett, white, yellow, blue, green)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RGB = [16, 20, 21]
LEDSTATUS = [[1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1]]

for pin in RGB:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

try:
    while True:
        for status in LEDSTATUS:
            print(status)
            for i in range(0, 3):
                GPIO.output(RGB[i], status[i])
            time.sleep(1.0)

except KeyboardInterrupt:
    print "Exiting"
    GPIO.cleanup()
