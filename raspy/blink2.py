import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN = 25
GPIO.setup(PIN,GPIO.OUT)

print "LED on"
GPIO.output(PIN,GPIO.HIGH)
time.sleep(2)
print "LED off"
GPIO.output(PIN,GPIO.LOW)

GPIO.cleanup()