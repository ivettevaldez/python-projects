"""
When programming, errors happen. It's just a fact of life. Perhaps the user gave bad input. 
Maybe a network resource was unavailable. Maybe the program ran out of memory. 
Or the programmer may have even made a mistake! Python's solution to errors are exceptions.

http://www.learnpython.org/en/Exception_Handling
"""

### EXAMPLES

print "### EXAMPLES"
def do_stuff_with_number(n):
	print n

the_list = (1, 2, 3, 4, 5)

for i in range(20):
	try:
		do_stuff_with_number(the_list[i])
	except IndexError:		# Raised when accessing a non-existing index of a list
		do_stuff_with_number(0)

"""
### EXERCISE

Should return the last name of the actor 
- think back to previous lessons for how to get it.
Handle all the exceptions!
"""
print "\n### EXERCISE"
actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
	try:
		return actor["name"].split()[1]
	except (RuntimeError, TypeError, NameError):
		print "Unexpected error"


get_last_name()
print "All exceptions caught! Good job!"
print "The actor's last name is %s" % get_last_name()

