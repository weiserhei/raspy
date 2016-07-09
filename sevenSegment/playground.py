#!/usr/bin/env python
# 7-Segment LCD playground

from tm1637_class import TM1637
import time

# pkill -9 -f /home/pi/python/sevenSegment/playground.py

## =============================================================
# -----------  Test -------------
BRIGHT_TYPICAL = 1
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

# Display.Show(halo)
# time.sleep(2)
Display.Clear()

# for i in range(len(topLoop)):
#     Display.Show1(3,topLoop[i])
#     sleep(0.5)
#
# sleep(1)
# Display.Clear()

while True:
    for i in range(len(sequence)):
        Display.Show(sequence[i])
        time.sleep(0.5)
