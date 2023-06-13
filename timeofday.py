import multiprocessing
import time
import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_time():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    timezone = now.strftime('%Z')
    response = {'time': time, 'timezone': timezone}
    return jsonify(response)

@app.route('/date', methods=['GET'])
def get_date():
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    response = {'date': date}
    return jsonify(response)

def cpu_intensive_task():
    while True:
        result = 0
        for i in range(100000000):
            result += i

@app.route('/increase_cpu', methods=['GET'])
def increase_cpu():
    process = multiprocessing.Process(target=cpu_intensive_task)
    process.start()
    return jsonify({'message': 'CPU usage increased'})

if __name__ == '__main__':
    app.run()
