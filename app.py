from flask import Flask, render_template, jsonify
import json

import RPi.GPIO as GPIO
import time, threading


app = Flask(__name__,
            template_folder = 'templates',
            static_folder='static')


alive = 0
data = {}


GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def get_distange():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/keep_alive', methods = ['GET', 'POST'])
def keep_alive():
    global alive, data
    alive += 1
    keep_alive_count = str(alive)
    data['keep_alive'] = keep_alive_count
    parsed_json = json.dumps(data)
    return str(parsed_json)


@app.route('/keep_alive_amin', methods = ['GET', 'POST'])
def keep_alive_amin():
    global alive, data
    alive += 1
    keep_alive_count = str(alive)
    data['keep_alive'] = keep_alive_count
    # parsed_json = json.dumps(data)
    return data


@app.route('/distange', methods = ['GET','POST'])
def distance():
    dist = get_distange()
    return jsonify(dist)


if __name__ == '__main__':
    # sensorsThread = threading.Thread(target = get_distange)
    # sensorsThread.start()
    app.run(host='10.56.241.222', port=8080, debug=True)
