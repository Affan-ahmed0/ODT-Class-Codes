from machine import Pin
import time

switch = Pin(3, Pin.OUT)

def blink():
    switch.on()
    time.sleep(0.02)
    switch.off()
    time.sleep(0.02)
    
blinknow= blink
n=0
for n in range(0,25):
    blinknow()
    n=n+1
    print (n)
