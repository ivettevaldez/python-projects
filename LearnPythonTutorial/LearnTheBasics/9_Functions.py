"""
Functions are a convenient way to divide your code into useful blocks, 
allowing us to order our code, make it more readable, reuse it and save some time. 
Also functions are a key way to define interfaces so programmers can share their code.

http://www.learnpython.org/en/Functions
"""

### EXAMPLES
def my_function():
	print "Hello from My Function!"

def my_function_with_args(username, greeting):
	print "Hello, %s, from My Function, I wish you %s" % (username, greeting)

def sum_two_numbers(a, b):
	return a + b

def call_the_example_functions():
	print "### Examples ###"
	# Print a simple greeting 
	my_function()

	# Prints - "Hello, John Doe, From My Function!, I wish you a great year!"
	my_function_with_args("John Doe", "a great year!")

	# After this line x will hold the value 3!
	x = sum_two_numbers(1,2)
	print "Value of x is %d" % x


"""
### EXERCISE

In this exercise you'll use an existing function, 
and while adding your own to create a fully functional program.

1. Add a function named list_benefits() that returns the following list of strings: 
"More organized code", "More readable code", "Easier code reuse", 
"Allowing programmers to share and connect code together".

2. Add a function named build_sentence(info) which receives a single argument 
containing a string and returns a sentence starting with the given string and ending 
with the string " is a benefit of functions!"

3. Run and see all the functions work together!
"""

# Modify this function to return a list of strings as defined in the instructions
def list_benefits():
	return ["More organized code", "More readable code", "Easier code reuse", 
	"Allowing programmers to share and connect code together"]
	pass

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
	return "%s is a benefit of functions!" % benefit
	pass

def name_the_benefits_of_functions():
	print "\n### Exercise ###"
	
	list_of_benefits = list_benefits()
	for benefit in list_of_benefits:
		print build_sentence(benefit)


call_the_example_functions()
name_the_benefits_of_functions()
