from gpiozero import RGBLED
import time
import random
from signal import pause

# active_high must be true because it is a common anode RGBLed
LED = RGBLED(red=17, green=18, blue=27, active_high=True)

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)

def traffic_light():
    while True:
        set_color(1, 0, 0)
        print("Red light")
        time.sleep(5)
        set_color(0, 1, 0)
        print("Green light")
        time.sleep(7)
        set_color(1, 1, 0)
        print("Yellow light")
        time.sleep(2)

        
def destroy():
    LED.close()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    traffic_light()
    try:
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()