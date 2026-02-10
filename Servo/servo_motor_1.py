from machine import Pin, PWM
from time import sleep

while True:
    Servo = PWM(Pin(19))
    Servo.freq(50)
    Servo.duty(45)
    sleep(0.2)
    Servo.duty(115)
    sleep(0.2)