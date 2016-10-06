"""
Decorators allow you to make simple modifications to callable objects 
like functions, methods, or classes. 
We shall deal with functions for this tutorial. 

http://www.learnpython.org/en/Decorators
"""

### EXAMPLES

print "### EXAMPLES"

# @decorator
# def functions(arg):
#     return "Return"

# # Is equivalent to:
# def function(arg):
#     return "Return"
# function=decorator(function) # This passes the function to the decorator, and reassigns it to the functions


def repeater(old_function):
    def new_function(*args, **kwds):	# See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds)		# We run the old function
        old_function(*args, **kwds)		# We do it twice
    return new_function					# We have to return the new_function, or it wouldn't reassign it to the value

@repeater
def Multiply(num1, num2):
    print num1*num2

Multiply(2, 3)

# You can also make it change the input, output, and do checking.
def Double_Out(old_function):
    def new_function(*args, **kwds):
        return 2*old_function(*args, **kwds)	# Modify the return value
    return new_function


def Double_In(old_function):
    def new_function(arg):						# Only works if the old function has one argument
        return old_function(arg*2)				# Modify the argument passed
    return new_function


def Check(old_function):
    def new_function(arg):
        if arg<0: 
        	raise ValueError, "Negative Argument"	# This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function


def Multiply(multiplier):
    def Multiply_Generator(old_function):
        def new_function(*args, **kwds):
            return multiplier*old_function(*args, **kwds)
        return new_function
    return Multiply_Generator		# It returns the new generator


@Multiply(3)	# Multiply is not a generator, but Multiply(3) is
def Num(num):
    return num

Multiply(3)


"""
### EXERCISE

Make a decorator factory which returns a decorator that decorates functions with one argument. 
The factory should take one argument, a type, and then returns a decorator that makes function 
should check if the input is the correct type. If it is wrong, it should print "Bad Type". 
(In reality, it should raise an error, but error raising isn't in this tutorial.) 
Look at the tutorial code and expected output to see what it is if you are confused 
(I know I would be.) Using isinstance(object, type_of_object) or type(object) might help.
"""
print "\n### EXERCISE"
def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print "Bad Type"
        return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print times2(2)
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print first_letter('Hello World')
first_letter(['Not', 'A', 'String'])

