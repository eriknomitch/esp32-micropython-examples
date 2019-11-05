import machine
import neopixel
import time
import random
import math

NP_PIN = 13
NP_COUNT = 24

np = neopixel.NeoPixel(machine.Pin(NP_PIN), NP_COUNT)

def chance(percentage):
    return random.randint(1, 100) >= percentage:

def demo(np):
    n = np.n

    for i in range(n):

        r = 0
        g = random.randint(0, 255)
        b = 0

        np[i] = (r, g, b)
        np.write()
        time.sleep_ms(10)

while True:
    demo(np)
