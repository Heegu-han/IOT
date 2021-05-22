import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print("Start!")

try:

    while True:
            input_state = GPIO.input(4)

            if input_state == False:
                print("on")

            else:
                print("off")

            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Bye!")
