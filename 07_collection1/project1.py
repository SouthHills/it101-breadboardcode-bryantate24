from gpiozero import Button
import subprocess
import time
from signal import pause

firefox_button = Button(18)
chromium_button = Button(23)

firefox = None
chromium = None

def setup():
    firefox_button.when_pressed = launch_firefox
    chromium_button.when_pressed = launch_chromium

def launch_firefox():
    global firefox
    if firefox is None:
        firefox = subprocess.Popen(["firefox"])
    else:
        firefox.terminate()
        firefox = None
    

def launch_chromium():
    global chromium
    if chromium is None:
        chromium = subprocess.Popen(["chromium-browser"])
    else:
        chromium.terminate()
        chromium = None

def destroy():
    firefox_button.close()
    chromium_button.close()

if __name__ == '__main__':     
    print ('Program is starting...')
    setup()
    try:
        pause()       
    except KeyboardInterrupt:  
        destroy()