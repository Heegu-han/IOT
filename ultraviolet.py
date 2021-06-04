import RPi.GPIO as GPIO
import time

motion_detector = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_detector, GPIO.IN)

try:
    while True:
        if GPIO.input(motion_detector) ==1:
            print("Motion Dectected")

        time.sleep(0.2)
except KeyboardInterrupt:
    print("Terminated by Keyboard")
finally:
    print("End of Program")
