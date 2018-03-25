import socket

class Moss:
"""
Inspired by moss.py a Python client for moss by Syed Chishti

and customized for OmegaUp.

Github:- https://github.com/soachishti/moss.py
"""

    SERVER = 'moss.stanford.edu'
    PORT = 7690 

	def __init__(self, language, submission_list):
		self.user_id = CONST
       	self.options = {
            "l": "",
            "m": 10,
            "d": 0,
            "x": 0,
            "c": "",
            "n": 250
        }
        self.options['l'] = language
        self.submissions = submission_list


    def run(self, queue):
        s = socket.socket()
        s.connect((self.server, self.port))

        s.send("moss {}\n".format(self.moss_id).encode())
        s.send("directory {}\n".format(self.options['d']).encode())
        s.send("X {}\n".format(self.options['x']).encode())
        s.send("maxmatches {}\n".format(self.options['m']).encode())
        s.send("show {}\n".format(self.options['n']).encode())
        s.send("language {}\n".format(self.options['l']).encode())

        recv = s.recv(1024)
        if recv == "no":
            s.send(b"end\n")
            s.close()

        for index, submission in iter(submissions):
        	filename = submission['problem_id'] + "_" +
        			   submission['username'] + "_" +
        			   submission['guid']

        	self.uploadFile(s, index+1, filename, submission['source'] )

        s.send("query 0 {}\n".format(self.options['c']).encode())

        response = s.recv(1024)
        s.send(b'end\n')
        s.close()

        link = response.decode().replace('\n', '')

        result = (self.language, link)
        queue.put(result)


    def uploadFile(self, s, file_id, filename, content):
    	size = len(content)
    	message = "file {0} {1} {2} {3}\n".format(
            file_id,
            self.options['l'],
            size,
            filename
        )
    	s.send(message.encode())
    	s.send(content)