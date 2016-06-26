# !/usr/bin/env python
# Author http://crazyice.net/?p=164
# Cycle RGB LED Colors (red, violett, blau, turqoise, green, white)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RGB = [16, 20, 21]
LEDSTATUS = [[1, 0, 0], [1, 0, 1], [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0], [1, 1, 1]]

# PWM_PINS = []

for pin in RGB:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

freq = 50
p = GPIO.PWM(RGB[0], freq)
# PWM_PINS.append(p)
p.start(0)


try:

    # starttime = time.time()
    # tick = 0.5
    ACTIVE_PWM_PINS = []

    while True:
            for status in LEDSTATUS:
                for i in range(0, 3):
                    GPIO.output(RGB[i], status[i])

                    # activePin = RGB[i]
                    # if RGB[i] in ACTIVE_PWM_PINS:
                    #     print("removing" + str(activePin))
                    #     ACTIVE_PWM_PINS.remove(activePin)
                    # if status[i] == 1:
                    #     ACTIVE_PWM_PINS.append(activePin)

                print("Lighting UP " + str(status))
                # Light up
                for i in range(100):
                    # for pin in ACTIVE_PWM_PINS:
                    p.ChangeDutyCycle(i)
                    time.sleep(0.02)

                print("Lighting DOWN " + str(status))
                # Dim down
                for i in range(100):
                    # for pin in ACTIVE_PWM_PINS:
                    p.ChangeDutyCycle(100 - i)
                    time.sleep(0.02)

            # main loop tick
            # sleep = tick - ((time.time() - starttime) % tick)
            # time.sleep(sleep)

            print("Cycle complete")
            time.sleep(2.0)

except KeyboardInterrupt:
    print "Exiting"
    # for pin in ACTIVE_PWM_PINS:
    # for pin in RGB:
    #     pin.stop(0)
    p.stop(0)
    GPIO.cleanup()
