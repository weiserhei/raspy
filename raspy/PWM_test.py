# !/usr/bin/env python
# Author: https://www.youtube.com/watch?v=uUn0KWwwkq8
# PWM on Pin
# To dim a LED

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINS = [27]
GPIO.setup(PINS[0], GPIO.OUT)

freq = 50
p = GPIO.PWM(PINS[0], freq)
p.start(0)

try:
    while True:

        # Light up
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(0.01)

        # Dim down
        for i in range(100):
            p.ChangeDutyCycle(100-i)
            time.sleep(0.01)

except KeyboardInterrupt:
    pass

p.stop()

GPIO.cleanup()
