from flask import Flask, request

import json 
from multiprocessing import Process, Queue

from Sherlock import main


app = Flask(__name__)

requests_queue = Queue()
processes = []

@app.route('/process/', methods =['POST'])
def process():
    """"
    Sample contest_data object:
    {
        'contest_id': 'ID of contest',
        'contest_naem': 'Name of contest',
        'submissions': [	# List of submissions of the contest
            {
            'user_id': 'id of user',
            'username': 'username of user',
            'problem_id': 'ID of problem',
            'language': 'Language user for submission eg c, py,etc',
            'guid': 'guid of run',
            'source': 'code for the submission'
            }
        ]
    }
    """
    # get JSON object from POST request by client
    contest_data = request.get_json()

    # put contest_data into queue
    # requests_queue.put(contest_data)

    if len(processes) < 4:
        p = Process(target=main.run, args=(requests_queue, processes))
        processes.append(p)
        p.start()

    return '200'





