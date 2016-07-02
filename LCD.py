from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD
import time
import RPi.GPIO as GPIO

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=4, en=17,
                       d4=18, d5=22, d6=23, d7=24,
                       cols=16, lines=2)
#http://www.mathias-wilhelm.de/arduino/beginner/schritt-6-lcd-displays/
# https://omerk.github.io/lcdchargen/
# lcd.set_cursor(0, 0)
lcd.home()
# Degree
# lcd.create_char(1, [0b01100,
#                    0b10010,
#                    0b10010,
#                    0b01100,
#                    0b00000,
#                    0b00000,
#                    0b00000,
#                    0b00000])
# # hourglass
# lcd.create_char(2, [0b11111,
#                    0b10001,
#                    0b01110,
#                    0b00100,
#                    0b01010,
#                    0b10001,
#                    0b11111,
#                    0b00000])
# dick
# lcd.create_char(3, [
#     0b00100,
#     0b01010,
#     0b01110,
#     0b01010,
#     0b01010,
#     0b11011,
#     0b10101,
#     0b11011
# ])

# ae
# lcd.create_char(4, [
#     0b01010,
#     0b00000,
#     0b01110,
#     0b00001,
#     0b01111,
#     0b10001,
#     0b01111,
#     0b00000
# ])
# smiley
# lcd.create_char(5, [
#     0b00000,
#     0b00000,
#     0b00000,
#     0b01010,
#     0b00000,
#     0b10001,
#     0b01110,
#     0b00000
# ])

# thumbsup
# lcd.create_char(6, [
#     0b00000,
#     0b00100,
#     0b01000,
#     0b01111,
#     0b11111,
#     0b11111,
#     0b00000,
#     0b00000
# ])


# lcd.message("Degrees: \x01")
# lcd.message("Smiley: \x03")
# lcd.message("\n")
# lcd.message("Hourglass: \x02")
# raw_input("Press Enter when ready\n>")
# lcd.message("Temperature: \n"+ chr(223)+ "C")
# sleep(10)

# char checkUmlaut(byte ascii) {
#     switch (ascii) {
#       case 228: return  225; break; // ae
#       case 246: return  239; break; // oe
#       case 252: return  245; break; // ue
#       case 223: return  226; break; // ss
#       case 176: return  223; break; // grad/degree
#       default:  return  ascii; break;
#   }
# }

lcd.message('                Hallo toby')
# lcd.set_cursor(16, 1)
# lcd.message('Lurch :-)')
# scroll text on display
for x in range(0, 24):
    lcd.move_right()
    sleep(.1)

sleep(2)

lcd.clear()

lcd.set_cursor(16, 0)
lcd.message("Blender ")
lcd.set_cursor(16, 1)
lcd.message("ftw \x06 \x05")
lcd.home()
lcd.set_cursor(16, 1)
# scroll text on display
for x in range(0, 16):
    lcd.move_left()
    sleep(.1)