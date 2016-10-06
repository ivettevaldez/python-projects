"""
Python provides built-in JSON libraries to encode and decode JSON.
In Python 2.5, the simplejson module is used, whereas in Python 2.7, the json module is used.

http://www.learnpython.org/en/Serialization
"""

### EXAMPLES

import json

def do_the_examples():
	print "### EXAMPLES"
	# To encode a data structure to JSON, use the "dumps" method. 
	json_string = json.dumps([1, 2, 3, "a", "b", "c"])
	# To load JSON back to a data structure, use the "loads" method.
	print json.loads(json_string)


	# Python supports a Python proprietary data serialization method called pickle (and a faster alternative called cPickle).
	import cPickle
	pickled_string = cPickle.dumps([1, 2, 3, "a", "b", "c"])
	print cPickle.loads(pickled_string)


"""
### EXERCISE

The aim of this exercise is to print out the JSON string with key-value pair "Me" : 800 added to it.
"""
def do_the_exercise():
	print "\n### EXERCISE"
	# Fix this function, so it adds the given name and salary pair to salaries_json, and return it
	def add_employee(salaries_json, name, salary):
		# Add your code here
		salaries = json.loads(salaries_json)
		salaries[name] = salary

		return json.dumps(salaries)
		
	# Test code
	salaries = '{"Alfred" : 300, "Jane" : 400 }'
	new_salaries = add_employee(salaries, "Me", 800)
	decoded_salaries = json.loads(new_salaries)
	print decoded_salaries["Alfred"]
	print decoded_salaries["Jane"]
	print decoded_salaries["Me"]


do_the_examples()
do_the_exercise()

