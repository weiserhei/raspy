# !/usr/bin/env python
# Author: Thiele
# Trigger on cable disconnect
# IMPORTANT! Both Pins connected to 3.3 V

from Adafruit_CharLCD import Adafruit_CharLCD
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcd = Adafruit_CharLCD(rs=4, en=17,
                       d4=18, d5=22, d6=23, d7=24,
                       cols=16, lines=2)

lcd.set_cursor(0, 0)
BUTTON1 = 27
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BUTTON2 = 20
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

start_time = 0

def startTimer(channel):

    print("Button 1 pressed!")
    lcd.message("Mutombo Start!")
    # start timer
    global start_time
    start_time = time.time()

    return


def stopTimer(channel):
    lcd.set_cursor(0, 1)
    elapsed_time = time.time() - start_time
    message = "Mutombo Stop! " + (str(elapsed_time))
    lcd.message(message)
    print(elapsed_time)
    GPIO.cleanup()

    return

GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=startTimer, bouncetime=300)
GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=stopTimer, bouncetime=300)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # print("ende gelaende")
    # elapsed_time = time.time() - start_time
    # print(elapsed_time)
    GPIO.cleanup()
