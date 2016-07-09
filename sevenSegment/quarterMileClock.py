#!/usr/bin/env python
# LCD + 7-Segment Quarter Mile Timer

from tm1637_class import TM1637
import time
from datetime import datetime
from Adafruit_CharLCD import Adafruit_CharLCD


lcd = Adafruit_CharLCD(rs=4, en=17,
                       d4=18, d5=22, d6=23, d7=24,
                       cols=16, lines=2)

def sevenSegDisplayTime(stamp):
    """Display Time on 7-Segment Display"""

    sevenSegTime = [
        HexDigits[int(stamp[3])],
        HexDigits[int(stamp[4])],
        HexDigits[int(stamp[6])],
        HexDigits[int(stamp[7])]
    ]

    Display.Show(sevenSegTime)

    return


def format_time(displayTime):
    """ Special function to format milliseconds
    http://stackoverflow.com/questions/11040177/python-datetime-round-trim-number-of-digits-in-microseconds"""
    # t = datetime.datetime.now()
    # s = t.strftime('%M:%S.%f')
    s = datetime.fromtimestamp(displayTime / 1000).strftime('%M:%S.%f')
    tail = s[-7:]
    f = round(float(tail), 2)
    temp = "%.2f" % f
    return "%s%s" % (s[:-7], temp[1:])

# pkill -9 -f /home/pi/python/sevenSegment/playground.py

## =============================================================
# -----------  Test -------------
BRIGHT_TYPICAL = 2
Display = TM1637(12, 16, BRIGHT_TYPICAL)

Alphabet = [0x77, 0x7c,
            0x58, 0x5e,
            0x79, 0x71,
            0x3D, 0x76, # h = 0x74
            0x10, 0x0e,
            0x70, 0x38,
            0x37, 0x54,
            0x5c, 0x73,
            0x67, 0x50,
            0x6d, 0x78,
            0x3e, 0x62,
            0x7e, 0x76,
            0x6e, 0x5b]

HexDigits = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7F, 0x6f, 0x77, 0x7c, 0x39, 0x5e, 0x79, 0x71]

halo = [0x76, 0x77, 0x38, 0x3F]
init = [0x10, 0x54, 0x10, 0x78]

# 1 Segment Snake Top Loop small
fourLoop = [0x01, 0x02, 0x40, 0x20]
# Filling top loop small
topLoop = [0x00, 0x01, 0x03, 0x43, 0x63]

# 2 Segment Snake Big One way
sequence = [0x00, 0x01, 0x03, 0x06, 0x0C, 0x18, 0x30, 0x20]

# 2 Segment Snake Big Loop
sequence = [0x03, 0x06, 0x0C, 0x18, 0x30, 0x21]

# 2 Segment Big Circle Loop
sequence = [
    [0x21, 0x00, 0x00, 0x00],
    [0x01, 0x01, 0x00, 0x00],
    [0x00, 0x01, 0x01, 0x00],
    [0x00, 0x00, 0x01, 0x01],
    [0x00, 0x00, 0x00, 0x03],
    [0x00, 0x00, 0x00, 0x06],
    [0x00, 0x00, 0x00, 0x0C],
    [0x00, 0x00, 0x08, 0x08],
    [0x00, 0x08, 0x08, 0x00],
    [0x08, 0x08, 0x00, 0x00],
    [0x18, 0x00, 0x00, 0x00],
    [0x30, 0x00, 0x00, 0x00]
]


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
displayTime = 0
lcd.message("3-2-1... GO")
Display.Show(halo)
time.sleep(2)
Display.Clear()

# try:
#     while True:
#         for i in range(len(topLoop)):
#             Display.Show1(0,topLoop[i])
#             time.sleep(0.5)
# except KeyboardInterrupt:
#     pass
Display.ShowDoublepoint(True)
Display.Show([0x3F, 0x3F, 0x3F, 0x3F])

raw_input("")

Display.Clear()

starttime = time.time() * 1000
lcd.clear()
lcd.set_cursor(0, 0)

while True:

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
    displayTime = millis - starttime
    stamp = format_time(displayTime)
    lcd.message("TIME: " + str(stamp))

    sevenSegDisplayTime(stamp)

    if displayTime > 6000:
        break

    time.sleep(0.09)

# exit
Display.ShowDoublepoint(False)
done = [0x5e, 0x5c, 0x54, 0x7B]
Display.Show(done)
time.sleep(3)
# Display.Clear()

while True:
    for i in range(len(sequence)):
        Display.Show(sequence[i])
        time.sleep(0.5)