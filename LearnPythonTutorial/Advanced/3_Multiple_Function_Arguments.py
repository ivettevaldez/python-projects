"""
Every function in Python receives a predefined number of arguments, if declared normally.
But, also it is possible to declare functions which receive a variable number of arguments...

http://www.learnpython.org/en/Multiple_Function_Arguments
"""

### EXAMPLES

print "### EXAMPLES"
# It is possible to declare functions which receive a variable number of arguments, using the following syntax:
# The "therest" variable is a list of variables, which receives all arguments which were given to the "foo" function after the first 3 arguments.
def foo(first, second, third, *therest):
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And all the rest... %s" % list(therest)

# It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, using the following syntax:
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)

    if options.get("number") == "first":
        return first


def do_the_examples():
	foo(1, 2, 3, 4, 5)
	result = bar(1, 2, 3, action = "sum", number = "first")
	print "Result: %d" % result



"""
### EXERCISE

Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) 
The foo function must return the amount of extra arguments received. The bar must return True 
if the argument with the keyword magicnumber is worth 7, and False otherwise.
"""
def do_the_exercise():
	print "\n### EXERCISE"
	# Edit the functions prototype and implementation
	def foo(a, b, c, *therest):
	    return len(therest)
	    pass

	def bar(a, b, c, **options):
	    if options.get("magicnumber") == 7:
	        return True
	    else:
	        return False
	    pass


	# Test code
	if foo(1,2,3,4) == 1:
	    print "Good."
	if foo(1,2,3,4,5) == 2:
	    print "Better."
	if bar(1,2,3,magicnumber = 6) == False:
	    print "Great."
	if bar(1,2,3,magicnumber = 7) == True:
	    print "Awesome!"


do_the_examples()
do_the_exercise()
