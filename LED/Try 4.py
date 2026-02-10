from machine import Pin
import time

L1 = Pin(3, Pin.OUT)
L2 = Pin(21, Pin.OUT)
L3 = Pin(19, Pin.OUT)
L4 = Pin(18, Pin.OUT)

def blink_L1():
    L1.on()
    time.sleep(0.02)
    L1.off()
    time.sleep(0.02)
    
def blink_L2():
    L2.on()
    time.sleep(0.02)
    L2.off()
    time.sleep(0.02)
    
def blink_L3():
    L3.on()
    time.sleep(0.02)
    L3.off()
    time.sleep(0.02)
    
def blink_L4():
    L4.on()
    time.sleep(0.02)
    L4.off()
    time.sleep(0.02)
    
BlinkL1= blink_L1
BlinkL2= blink_L2
BlinkL3= blink_L3
BlinkL4= blink_L4

n=0
for n in range(0,25):
    BlinkL1()
    BlinkL2()
    BlinkL3()
    BlinkL4()
    n=n+1
    print (n)

