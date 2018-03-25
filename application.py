from flask import Flask, request

from queue import Queue
from threading import Thread
from multiprocessing import Process, Queue

import json 
from Sherlock.main import run
from Sherlock.request import Request

app = Flask(__name__)

control_queue = Queue()
processes = []

def worker():
	sherlock_main(contest_data)



@app.route('/process/', methods =['POST'])
def process():
    contest_data = request.get_json()

    # put contest_data into queue
    control_queue.put(data_data)

    if len(processes) < 4:
    	p = Process(target=sherlock_main.run, args=(control_queue,))
    	processes.append(p)
    	p.start()

    return '200'





