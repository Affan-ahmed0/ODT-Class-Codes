from machine import Pin
from time import sleep
Sensor = Pin(15,Pin.IN, Pin.PULL_UP)
Light = Pin(27,Pin.OUT)
while True:
    sleep(0.05)
    print(Sensor.value())
    if Sensor.value() ==0:
        Light.on()
        sleep(0.05)
        Light.off()
    else:
        Light.off()
        