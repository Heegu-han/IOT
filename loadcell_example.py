import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

# Force Python 3 ###########################################################

if sys.version_info[0] != 3:
    raise Exception("Python 3 is required.")

############################################################################


hx = HX711(5, 6)


def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()


def setup():
    """
    code run once
    """
    hx.set_offset(`Place offset here`)
    hx.set_scale(`Place ratio here`)


def loop():
    """
    code run continuosly
    """

    try:
        val = hx.get_grams()
        print(val)

        hx.power_down()
        time.sleep(.001)
        hx.power_up()

        time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()


##################################

if __name__ == "__main__":

    setup()
    while True:
        loop()
