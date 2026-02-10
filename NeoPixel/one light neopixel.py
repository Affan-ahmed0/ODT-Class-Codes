from machine import Pin
import neopixel
from time import sleep

np = neopixel.NeoPixel(Pin(21),16)
np[0]= (0,128,128)
np.write()
print("Cyan")
sleep(0.2)
np[0]= (0,0,0)
print("Off")
np.write()
