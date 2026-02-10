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
    sleep(0.05)
    
while True:
    n=0
    while n<16:
        np[n] = (0,0,255)
        np.write()
        sleep(0.05)
        np[n] = (0,0,0)
        np.write()
        sleep(0.05)
        n=n+1
