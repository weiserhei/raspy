# !/usr/bin/env python
from __future__ import division
from subprocess import PIPE, Popen
from Adafruit_CharLCD import Adafruit_CharLCD
# import time
# import RPi.GPIO as GPIO
import socket

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=4, en=17,
                       d4=18, d5=22, d6=23, d7=24,
                       cols=16, lines=2)

# http://www.quinapalus.com/hd44780udg.html
# https://omerk.github.io/lcdchargen/

# Degree
# lcd.create_char(1, [0b01100,
#                    0b10010,
#                    0b10010,
#                    0b01100,
#                    0b00000,
#                    0b00000,
#                    0b00000,
#                    0b00000])


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

#Stackoverflow solution
# ipaddr = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
# run_cmd already adds \n to the output
ipaddr = run_cmd(cmd)


def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])


cpu_temperature = get_cpu_temperature()
message = "IP: " + str(ipaddr) + "Temp: " + str(get_cpu_temperature()) + chr(223) + "C"

lcd.message(message)
print(message)

# lcd.enable_display(False)