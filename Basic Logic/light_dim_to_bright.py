from machine import Pin,PWM
from time import sleep

Light = PWM(4)

n=2
while n<=9:
    a=2**n
    Light.freq(100)
    Light.duty(a)
    n=n+1
    sleep(0.05)
