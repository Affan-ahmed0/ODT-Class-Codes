from machine import Pin
import neopixel
from time import sleep

sensorup = Pin(15,Pin.IN, Pin.PULL_UP)
sensorleft = Pin(4,Pin.IN, Pin.PULL_UP)
sensordown = Pin(5,Pin.IN, Pin.PULL_UP)
sensorright = Pin(18,Pin.IN, Pin.PULL_UP)
np = neopixel.NeoPixel(Pin(19),16)

def up_on():
    if sensorup.value() == 0:
        np[8] = (0,0,255)
        np[7] = (0,0,255)
        np[9] = (0,0,255)
        np[6] = (0,0,255)
        np[10] = (0,0,255)
        np.write()

def up_off():
    if sensorup.value() == 1:
        np[8] = (0,0,0)
        np[7] = (0,0,0)
        np[9] = (0,0,0)
        np[6] = (0,0,0)
        np[10] = (0,0,0)
        np.write()
        
def left_on():
    if sensorleft.value() == 0:
        np[12] = (0,0,255)
        np[11] = (0,0,255)
        np[13] = (0,0,255)
        np[10] = (0,0,255)
        np[14] = (0,0,255)
        np.write()
        
def left_off():
    if sensorleft.value() == 1:
        np[12] = (0,0,0)
        np[11] = (0,0,0)
        np[13] = (0,0,0)
        np[10] = (0,0,0)
        np[14] = (0,0,0)
        np.write()
def right_on():
    if sensorright.value() == 0:
        np[4] = (0,0,255)
        np[5] = (0,0,255)
        np[3] = (0,0,255)
        np[10] = (0,0,255)
        np[14] = (0,0,255)
        np.write()
def right_off():
    if sensorright.value() == 1:
        np[4] = (0,0,0)
        np[5] = (0,0,0)
        np[3] = (0,0,0)
        np[10] = (0,0,0)
        np[14] = (0,0,0)
        np.write()
def down_on():
    if sensordown.value() == 0:
        np[0] = (0,0,255)
        np[1] = (0,0,255)
        np[15] = (0,0,255)
        np[2] = (0,0,255)
        np[14] = (0,0,255)
        np.write()
def down_off():
    if sensordown.value() == 1:
        np[0] = (0,0,0)
        np[1] = (0,0,0)
        np[15] = (0,0,0)
        np[2] = (0,0,0)
        np[14] = (0,0,0)
        np.write()

while True:
    up_on()
    left_on()
    sleep(0.2)
    up_off()
    left_off()

    
    

