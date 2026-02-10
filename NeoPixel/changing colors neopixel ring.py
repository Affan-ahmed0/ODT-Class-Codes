from machine import Pin
from time import sleep
import neopixel

np = neopixel.NeoPixel(Pin(21),16)

def blue():
    np[n] = (0,0,255)
    np.write()
    sleep(0.05)
    np[n] = (0,0,0)
    np.write()
def green():
    np[n] = (0,255,0)
    np.write()
    sleep(0.05)
    np[n] = (0,0,0)
    np.write()
def red():
    np[n] = (255,0,0)
    np.write()
    sleep(0.05)
    np[n] = (0,0,0)
    np.write()
    
while True:
    n=0
    while n<16:
        blue()
        n=n+1
        blue()
        n=n+1

