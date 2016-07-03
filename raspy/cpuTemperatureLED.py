# !/usr/bin/env python
# coding=utf-8
# Author: weiserhei
# CPU Temperature LED Traffic Light
# From green to red to blinking on raising CPU Temp.

# import psutil
import RPi.GPIO as GPIO
from subprocess import PIPE, Popen
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = 4
yellow = 17
green = 27

PINS = [red, yellow, green]

for p in PINS:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.LOW)


def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])


def blink(switch_off):

    if switch_off:
        GPIO.output(red, GPIO.HIGH)
        GPIO.output(green, GPIO.HIGH)
        GPIO.output(yellow, GPIO.HIGH)
    else:
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(yellow, GPIO.LOW)
    return


def setHigh(value):

    GPIO.output(red, GPIO.HIGH)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(yellow, GPIO.LOW)
    output = "Temp High"

    return output


def setMedium(value):

    GPIO.output(yellow, GPIO.HIGH)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    output = "Temp Medium"

    return output


def setLow(value):

    GPIO.output(green, GPIO.HIGH)
    GPIO.output(red, GPIO.LOW)
    GPIO.output(yellow, GPIO.LOW)
    output = "Temp Low"

    return output


def main():

    starttime = time.time()
    tick = 0.5
    lastTick = 0
    lastUpdate = 0
    percent = 0
    sleep = 0
    blinking = False

    thresholds = [55, 60, 65, 70]

    try:

        while True:

            lastTick += tick
            if lastTick > 2:
                lastTick = 0
                # percent = psutil.cpu_percent()
                percent = get_cpu_temperature()
                blinking = False
                os.system('clear')

                if percent <= thresholds[0]:
                    output = setLow(percent)
                # elif percent > 55 and percent < 60:
                elif thresholds[0] < percent < thresholds[1]:
                    output = setMedium(percent)
                elif thresholds[1] < percent < thresholds[2]:
                    output = setHigh(percent)
                elif percent >= thresholds[3]:
                    blinking = True
                    output = "Alarm"

                print output + ": " + str(percent) + "°C"

            # tick faster for blink
            lastUpdate += sleep
            if blinking:
                switch_off = lastUpdate > 0.5
                blink(switch_off)
                if switch_off:
                    lastUpdate = 0

            # main loop tick
            sleep = tick - ((time.time() - starttime) % tick)
            time.sleep(sleep)

    except KeyboardInterrupt:
        print("")
        print("Exiting, cleaning up...")
        for p in PINS:
            GPIO.output(p, GPIO.LOW)
        GPIO.cleanup()


if __name__ == '__main__':
    main()
