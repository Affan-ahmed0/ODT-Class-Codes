from machine import Pin,PWM
from time import sleep

Light = PWM(4)

#X = input("Time on:")
#Y = input("Time off:")

Light.freq(1000) #How often it switches on and off; Hertz
Light.duty(756) #The cap of the voltage