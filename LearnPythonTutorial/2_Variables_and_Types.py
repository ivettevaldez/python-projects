"""
Python is completely object oriented, and not "statically typed". 
You do not need to declare variables before using them, 
or declare their type. Every variable in Python is an object.

This tutorial will go over a few basic types of variables.

http://www.learnpython.org/en/Variables_and_Types
"""

### EXAMPLES

print "### EXAMPLES"
# To define an integer, use the following syntax:
myint = 7
print "myint equals " + str(myint)

# To define a floating point number, you may use one of the following notations:
myfloat = 7.0
myfloat = float(7)
print "myfloat equals " + str(myfloat)

# Strings are defined either with a single quote or a double quotes.
mystring1 = 'Hello, '
mystring1 = "Hello, "

"""
The difference between the two is that using double quotes 
makes it easy to include apostrophes (whereas these would 
terminate the string if using single quotes.
"""
mystring2 = "don't worry about apostrophes"
print mystring1 + mystring2

# Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print three

hello = "Hello"
world = "World"
helloworld = hello + " " + world
print helloworld

# Assignments can be done on more than one variable "simultaneously" on the same line:
a, b = 3, 4


"""
### EXERCISE

The target of this exercise is to create a string, an integer, and a floating point number. 
The string should be named mystring and should contain the word "hello". 
The floating point number should be named myfloat and should contain the number 10, 
and the integer should be named myint and should contain the number 20.
"""
print "\n### EXERCISE"

# Your code goes here
mystring = "hello"
myfloat = 10.0
myint = 20

# Testing code
if mystring == "hello":
    print "String: %s" % mystring
if isinstance(myfloat, float) and myfloat == 10.0:
    print "Float: %d" % myfloat
if isinstance(myint, int) and myint == 20:
    print "Integer: %d" % myint

