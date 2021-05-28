from flask import Flask
from flask import request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

@app.route('/')
def index():
    return '<h1>Hello LED IoT!</h1>'

@app.route('/led')
def led_control():
    ctrl = request.args.get('ctrl')
    if ctrl == 'on':
        GPIO.output(4,True)
        result = '<h1>LED ON</h1>'
    elif ctrl == 'off':
        GPIO.output(4,False)
        result = '<h1>LED OFF</h1>'
    else:
        result = "Wrong Parameter!"
    return result

if __name__ == "__main__":
    try:
        app.run(host="192.168.137.5",port=5001,debug=True)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
