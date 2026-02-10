from machine import Pin
from time import sleep
import neopixel
from random import randint
np = neopixel.NeoPixel(Pin(19),16)

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
def turquoise():
    np[n] = (0,122,255)
    np.write()
    sleep(0.05)
    np[n] = (0,0,0)
    np.write()
def cyan():
    np[n] = (0,122,122)
    np.write()
    sleep(0.05)
    np[n] = (0,0,0)
    np.write()
def blue_low():
    np[n] = (0,60,60)
    np.write()
    sleep(0.05)
    np[n] = (0,0,0)
    np.write()
def blue_lower():
    np[n] = (0,30,30)
    np.write()
    sleep(0.05)
    np[n] = (0,0,0)
    np.write()
def white():
    np[n] = (255,255,255)
    np.write()
    sleep(0.05)
    np[n] = (0,0,0)
    np.write()   

    
while True:
    n=0
    while n<16:
        blue()
        n=n+1
        turquoise()
        n=n+1
        white()
    n=n+1


