#!/usr/bin/env python
# Stopwatch with progress

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
import time

from datetime import datetime

lcd = Adafruit_CharLCD(rs=4, en=17,
                       d4=18, d5=22, d6=23, d7=24,
                       cols=16, lines=2)


def format_time():
    """ Special function to format milliseconds
    http://stackoverflow.com/questions/11040177/python-datetime-round-trim-number-of-digits-in-microseconds"""
    # t = datetime.datetime.now()
    # s = t.strftime('%M:%S.%f')
    s = datetime.fromtimestamp(displayTime / 1000).strftime('%M:%S.%f')
    tail = s[-7:]
    f = round(float(tail), 2)
    temp = "%.2f" % f
    return "%s%s" % (s[:-7], temp[1:])


def increasePosition(value):

    displayLength = 10

    # Loop through the distance line
    if value > displayLength:
        rest = divmod(value, displayLength)
        value -= rest[0] * displayLength

    output = ""
    for i in range(value):
        output += "-"
    output += ">"
    for i in range(value + 1, displayLength - value + 1):
        output += "-"

    return output


distance = 0
counter = 0
lcd.message("3-2-1... GO")
# raw_input("")

starttime = time.time() * 1000
# s, ms = divmod(1236472051807, 1000)  # (1236472051, 807)
lcd.clear()
lcd.set_cursor(0, 0)

while 1:
    if counter == 0:
        counter = 10
        lcd.set_cursor(0, 1)
        # lcd.message("METER: " + str(0))
        # lcd.message("---------->-----")
        asciiPosition = increasePosition(distance)
        lcd.message("DIST: " + asciiPosition)
        distance += 1
    counter -= 1

    lcd.set_cursor(0, 0)
    millis = int(round(time.time() * 1000))
    # lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
    displayTime = millis - starttime
    # stamp = datetime.fromtimestamp(displayTime).strftime('%H:%M:%S')
    # stamp = datetime.fromtimestamp(displayTime / 1000).strftime('%M:%S:%f')
    stamp = format_time()
    # stamp = '%s.%03d' % (time.strftime('%H:%M:%S', time.gmtime(s)), ms)
    lcd.message("TIME: " + str(stamp))
    time.sleep(0.1)
