from machine import Pin
from time import sleep
from random import randint

B1 = Pin(21,Pin.IN,Pin.PULL_UP)
B2 = Pin(18,Pin.IN,Pin.PULL_UP)
n=0
while True:
    x = B1.value()
    y = B2.value()
    if x==0 and y==0:
        print("Counter Reset")
        n=0
    elif x==0:
        print(n+1)
        n = n+1
    elif y==0:
        print(n-1)
        n = n-1
    sleep(0.2)
    
    

