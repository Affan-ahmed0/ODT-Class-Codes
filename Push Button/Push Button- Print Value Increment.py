from machine import Pin
from time import sleep
from random import randint

B1 = Pin(21,Pin.IN,Pin.PULL_UP)
n=0
while True:
    x = B1.value()
    while x==1:
        sleep(0.2)
        print("off")
        if x==0:
            print(n)
            n = n+1
            print("on")
sleep(0.2)
