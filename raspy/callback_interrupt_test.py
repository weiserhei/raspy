# !/usr/bin/env python
# Author: http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
# Test Callback and Interrupt
# IMPORTANT! BUTTON1 must be connected to 3.3V Source

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

BUTTON1 = 17
BUTTON2 = 27

GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def printFunction(channel):

    print("Button 1 pressed!")
    print("Note how the bouncetime affects the button press")
    return

GPIO.add_event_detect(BUTTON1, GPIO.RISING, callback=printFunction, bouncetime=300)

while True:

    GPIO.wait_for_edge(BUTTON2, GPIO.FALLING)
    print("Button 2 Pressed")
    GPIO.wait_for_edge(BUTTON2, GPIO.RISING)
    print("Button 2 Released")

GPIO.cleanup()
