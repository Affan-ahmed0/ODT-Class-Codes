from machine import Pin, TouchPad
import time

Blue = Pin(3, Pin.OUT)
Board = Pin(2,Pin.OUT)

touch = TouchPad(Pin(12))

while True:
    value_touch = touch.read()
    print("Current Touch Value=",value_touch)
    time.sleep(0.2)
    if value_touch <= 200:
        Blue.on()
        Board.on()
        print("Turned On")
        time.sleep(0.05)
    else :
        Blue.off()
        Board.off()
        print("Turned Off")
    Blue.off()
    Board.off()

