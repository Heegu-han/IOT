import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER=18
GPIO_ECHO=24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER,True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)

    while GPIO.input(GPIO_ECHO)==0:
        start_time=time.time()

    while GPIO.input(GPIO_ECHO)==1:
        start_time=time.time()
    time_elasped=stop_time-start_time

    distance=(time_elasped*34300)/2

    return distance

if __name__=='__main__':

    try:
        while True:
            dist =distance()
            print(f"Measured Disatance = {dist} cm")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")

    finally:
        GPIO.cleanup()
