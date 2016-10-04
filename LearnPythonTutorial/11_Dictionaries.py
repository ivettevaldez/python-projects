"""
A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. 
Each value stored in a dictionary can be accessed using a key, which is any type of object 
(a string, a number, a list, etc.) instead of using its index to address it.

http://www.learnpython.org/en/Dictionaries
"""

### EXAMPLES

def create_phonebook():
	# For example, a database of phone numbers could be stored using a dictionary like this:
	phonebook = {}
	phonebook["John"] = 938477566
	phonebook["Jack"] = 938377264
	phonebook["Jill"] = 947662781

	# Alternatively, a dictionary can be initialized with the same values in the following notation:
	phonebook = {
		"John" : 938477566,
		"Jack" : 938377264,
		"Jill" : 947662781
	}
	return phonebook


def print_phone_numbers(phonebook):
	for name, number in phonebook.iteritems():
		print "Phone number of %s is %d" % (name, number)
	else:
		print "\n"


def do_the_examples():
	print "### EXAMPLES"
	phonebook = create_phonebook()
	print_phone_numbers(phonebook)

	"""
	That will print:
	Phone number of Jill is 947662781
	Phone number of John is 938477566
	Phone number of Jack is 938377264
	"""

	del phonebook["John"]
	phonebook.pop("Jill")

	print_phone_numbers(phonebook)

	"""
	Now will print:
	Phone number of Jack is 938377264
	"""


"""
### EXERCISE

Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
"""
def do_the_exercise():
	print "### EXERCISE"

	phonebook = {
	    "John" : 938477566,
	    "Jack" : 938377264,
	    "Jill" : 947662781
	}

	# Write your code here
	phonebook["Jake"] = 938273443
	del phonebook["Jill"]


	# Testing code
	if "Jake" in phonebook:
	    print "Jake is listed in the phonebook."
	if "Jill" not in phonebook:
	    print "Jill is not listed in the phonebook."


do_the_examples()
do_the_exercise()

