from machine import Pin
import time

L1 = Pin(3, Pin.OUT)
L2 = Pin(21, Pin.OUT)
L3 = Pin(19, Pin.OUT)
L4 = Pin(2, Pin.OUT)

while True:
    L1.on()
    L2.on()
    L3.on()
    L4.on()
    time.sleep(0.4)
    L1.off()
    L2.off()
    L3.off()
    L4.off()



