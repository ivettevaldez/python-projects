"""
A Closure is a function object that remembers values in enclosing scopes 
even if they are not present in memory.

http://www.learnpython.org/en/Closures
"""


### EXAMPLES
"""
Firstly, a Nested Function is a function defined inside another function. 
Its very important to note that the nested functions can access the variables 
of the enclosing scope. However, at least in python, they are only readonly. 
However, one can use the "nonlocal" keyword explicitly with these variables 
in order to modify them.
"""
def transmit_to_space_1(message):
    print "This is the enclosing function"
    def data_transmitter():
        print "The nested function"
        print message
    data_transmitter()

# To demonstrate the use of the "nonlocal" keyword, consider this:
def print_msg(number):
    def printer():
        print "Here we are using the nonlocal keyword"
        # nonlocal number		# Only works in Python 3, we're using version 2.7
        # number = 3
        print number
    printer()
    print number

# How about we return the function object rather than calling the nested function within.
def transmit_to_space_2(message):
    print "This is the enclosing function"
    def data_transmitter():
        print "The nested function"
        print(message)
    return data_transmitter


def do_the_examples():
	print "### EXAMPLES"
	transmit_to_space_1("The message!")
	print_msg(9)

	"""
	Even though the execution of the "transmit_to_space()" was completed, 
	the message was rather preserved. This technique by which the data 
	is attached to some code even after end of those other original functions 
	is called as closures in Python.

	ADVANTAGE : Closures can avoid use of global variables and provides 
	some form of data hiding.(Eg. When there are few methods in a class, 
	use closures instead).
	"""
	fun2 = transmit_to_space_2("Burn the Sun!")
	fun2()


"""
### EXERCISE

Make a nested loop and a python closure to make functions to get 
multiple multiplication functions using closures. That is using closures, 
one could make functions to create multiply_with_5() or multiply_with_4() 
functions using closures.
"""
# Your code goes here
def multiplier_of(a):
    def do_the_math(b):
        return a * b
    return do_the_math
    
def do_the_exercise():
	print "\n### EXERCISE"
	multiplywith5 = multiplier_of(5)
	print multiplywith5(9)


do_the_examples()
do_the_exercise()

