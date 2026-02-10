from machine import Pin
import time

Button = Pin(3,Pin.IN, Pin.PULL_UP)

while True:
    time.sleep(0.4)
    print(Button.value())
    if Button.value() == 0:
        print("Yayy")
    else:
        print("NOOOO!!")
