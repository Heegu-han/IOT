import RPi.GPIO as GPIO
import time

motion_detector = 4
led = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_detector, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        if GPIO.input(motion_detector) ==1:
            GPIO.output(led, True)
        else:
            GPIO.outpuy(led, False)

        time.sleep(0.2)
except KeyboardInterrupt:
    print("Terminated by Keyboard")
finally:
    print("End of Program")
