import sys

from Sherlock.Database_helper import update_request_status
from Sherlock.Request import Request
from Sherlock.MOSS.connection import Moss
from queue import Queue


def run_moss(request):
	"""
	This method will run moss on the contest.
	We need to send data to MOSS seperately for every
	programming language used in the contest as MOSS
	does not support multiple programming languages.

	This method will return a list of tuples containing
	the name of language and report link for that language.
	Eg:
	[('c', 'http://moss.stanford.edu/report/134554'),
	 ('py', 'http://moss.stanford.edu/report/123123'),
	 ('pascal', 'http://moss.stanford.edu/report/345344')]
	"""
	processes = []
	reports = []
	queue = Queue()
	for language, submission_list  in request.submissions.iteritems():
		moss = Moss(language, submission_list)
		moss.run(queue)

	return reports

def write_json_report(request, json_report):
	"""
	This method will write the JSON report to memory.
	at location similar to
	/var/lib/omegaup/plagiarism/{contest_id % 100}/{contest_id}
	"""
	# TODO
	pass

def run(control_queue):

	# get data from contest queue to process
	contest_data = control_queue.get()

	# create a Request object from contest_data
	request = Request(contest_data)

	# update the Request object and add the list of reports generated by MOSS
	# list of reports generated by moss, sectioned as per language
	# Eg: [('c', 'http://moss.stanford.edu/report/1345546'), ('py', 'http://moss.stanford.edu/report/123123')]
	request.moss_report_url = run_moss(request)

	# Pass on the request object to Parser to generate a JSON report
	parser = Parser(request)
	json_report = parser.get_json_report()

	# Write the generated JSON report to memory
	write_json_report(request, json_report)

	# Update 'report_status' in database to 'Created'
	update_report_status(request.get_contest_id(), 'CREATED')


