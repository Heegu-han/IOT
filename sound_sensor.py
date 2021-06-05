import RPi.GPIO as GPIO
import time

sound_detector=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound_detector,GPIO.IN,pull_up_down=GPIO.PUD_UP)

time.sleep(5)

try:
    while True:
        if GPIO.input(sound_detector)==GPIO.LOW:
            print("Noisy")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Measurement stopped by User")

finally:
    GPIO.cleanup()
