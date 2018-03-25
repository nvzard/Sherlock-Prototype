
class Parser():
	"""
	Takes the request object and generates a JSON report
	by leveraging the webpages hosted at MOSS's servers
	"""

	# TODO
	
	def __init__(self, request):
		self.contest_id = request.get_contest_id()
		self.contest_name = request.get_contest_name()
		self.moss_reports = request.get_moss_reports()

