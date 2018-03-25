

class Request():

	def __init__(self, contest_object):
		self.contest_id = contest_object['contest_id']
		self.contest_name = contest_object['contest_name']
		# dict of submissions based on language supported bu moss
		self.submissions = Request.sort_submissions(contest_object['submissons'])
		self.moss_report_url = None

	@staticmethod
	def sort_submissions(submissions):
	'''
	Returns dictionary of submissions grouped
	with respect to the language. Each language
	key will contain list of user submission
	objects. Eg:
	{
		"c":[
			{		'user_id': '1',
				 	'user_name': 'user123',
				 	'problem_id': '123',
				 	'guid': '2f38h3',
				 	'source': '#include<stdio.h>\n#include<stdlib.h>'			
			}
		],

		"python":[{
					'user_id': '2',
				 	'user_name': 'user321',
				 	'problem_id': '342',
				 	'guid': '7hf9ed',
				 	'source': 'import sys\nimport os\n def main():\n\tprint("Hello")\n'				
				}
			]
	}

	'''

		result = defaultdict(list)

		for submission in submissions:
			# discard submissions not supported by MOSS
			if submission['language'] not in format_dict:
				continue

			# append in a dict divided by languages
			# convert file extensions to MOSS language keywords
			result[format_dict[submission['language']]].append(
				{'user_id': submission['user_id'],
				 'user_name': submission['user_name'],
				 'problem_id': submission['problem_id'],
				 'guid': submission['guid'],
				 'source': submission['source']
				}
			)

		return result



