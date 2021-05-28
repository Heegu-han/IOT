from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

@app.route('/')
def index():
    return '<h1>Hello LED IoT!</h1>'

@app.route('/on')
def led_on():
    GPIO.output(4,True)
    return '<h1>LED ON</h1>'

@app.route('/off')
def led_off():
    GPIO.output(4,False)
    return '<h1>LED OFF</h1>'

if __name__ == "__main__":
    try:
        app.run(host="192.168.137.5",port=5001,debug=True)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
