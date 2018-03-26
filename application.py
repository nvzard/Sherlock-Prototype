from flask import Flask, request

import json 
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

from Sherlock import main


app = Flask(__name__)

executor = ThreadPoolExecutor(2)
requests_queue = Queue()


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
    requests_queue.put(contest_data)

    executor.submit(main.run, requests_queue)

    return '200'





