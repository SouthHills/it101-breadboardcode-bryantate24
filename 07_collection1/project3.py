from gpiozero import RGBLED, Button
import time
import random
from signal import pause
import sys

# active_high must be true because it is a common anode RGBLed
LED = RGBLED(red=17, green=18, blue=27, active_high=True)
BUTTON = Button(24)

RED = (1, 0, 0)
GREEN = (0, 1, 0)

all_colors = [
    RED, # Red
    (0, 0, 1), # Blue
    (1, 1, 0), # Yellow
    GREEN # Green
]

button_pressed = False
showing_green = False
game_over = False

def setup():
    global BUTTON
    BUTTON.when_pressed = user_input

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)
    
def cycle_colors():
    global showing_green
    while button_pressed == False:
        color = random.choice(all_colors)
        set_color(color[0], color[1], color[2])
        
        if(color == GREEN):
            showing_green = True
            break
        
        time.sleep(random.random() * 2 + 0.2)
        
    while game_over == False:
        time.sleep(0.1)
        
def user_input():
    global showing_green, button_pressed, game_over
    button_pressed = True
    if showing_green:
        print("You win")
    else:
        print("You lose!")
        
    flash_color: tuple
    
    if showing_green:
        flash_color = GREEN
    else:
        flash_color = RED
    
    for n in range(0, 5):
        set_color(flash_color[0], flash_color[1], flash_color[2])
        time.sleep(0.5)
        set_color(0,0,0)
        time.sleep(0.5)
    
    game_over = True

def destroy():
    LED.close()
    BUTTON.close()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        cycle_colors()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
