# max7219demo.py
# Demo setting a random number of LEDs on or off at a random intervals using
# the https://github.com/adafruit/micropython-adafruit-max7219
# module using the hardware SPI on a WemosD1 mini
from machine import Pin, SPI
import max7219
import time
import uos

# Light up or turn off up MAX_LEDS at a time
MAX_LEDS = 10
MAX_UPDATE_TIME = 10

hspi = SPI(1, baudrate=10000000, polarity=0, phase=0)
display = max7219.Matrix8x8(hspi, Pin(15))

display.brightness(7)

# Turn of all leds
display.fill(0)
display.show()

rand = bytearray(3)

while True:
    for _ in range(uos.urandom(1)[0] % MAX_LEDS):
        # get 3 random bytes and use them to get x, y and ON or OFF
        rand = uos.urandom(3)
        display.pixel(rand[0] % 8, rand[1] % 8, rand[2] % 2)
    display.show()
    time.sleep(uos.urandom(1)[0] % MAX_UPDATE_TIME)
