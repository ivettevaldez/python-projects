"""
Sets are lists with no duplicate entries. 

http://www.learnpython.org/en/Sets
"""

### EXAMPLES

def do_the_examples():
	print "### EXAMPLES"
	# This will print out a list containing "my", "name", "is", "Eric", and finally "and":
	print set("my name is Eric and Eric is my name".split())

	a = set(["Jake", "John", "Eric"])
	b = set(["John", "Jill"])

	# To find out which members attended both events:
	print a.intersection(b)				# Prints out set(['John'])
	print b.intersection(a)				# Prints out set(['John'])

	# To find out which members attended only one of the events:
	print a.symmetric_difference(b)		# Prints out set(['Jill', 'Jake', 'Eric'])
	print b.symmetric_difference(a)		# Prints out set(['Jill', 'Jake', 'Eric'])

	# To find out which members attended only one event and not the other
	print a.difference(b)				# Prints out set(['Jake', 'Eric'])
	print b.difference(a)				# Prints out set(['Jill'])

	# To receive a list of all participants:
	print a.union(b)					# Prints out set(['Jill', 'Jake', 'John', 'Eric'])


"""
### EXERCISE

In the exercise below, use the given lists to print out a set containing 
all the participants from event A which did not attend event B.
"""
def do_the_exercise():
	print "\n### EXERCISE"
	a = ["Jake", "John", "Eric"]
	b = ["John", "Jill"]

	print set(a).difference(set(b))


do_the_examples()
do_the_exercise()

