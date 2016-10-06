"""
Python uses boolean variables to evaluate conditions. 
The boolean values True and False are returned when an expression is compared or evaluated.

http://www.learnpython.org/en/Conditions
"""

### EXAMPLES

print "### EXAMPLES"
x = 2
print x == 2 	# Prints out True
print x == 3 	# Prints out False
print x < 3  	# Prints out True

# Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print "Your name is John, and you are also 23 years old."

if name == "John" or name == "Rick":
    print "Your name is either John or Rick."

# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:
if name in ["John", "Rick"]:
    print "Your name is either John or Rick."

"""
Python uses indentation to define code blocks, instead of brackets. 
The standard Python indentation is 4 spaces, although tabs and any other space size will work, 
as long as it is consistent. Notice that code blocks do not need any termination.

Here is an example for using Python's "if" statement using code blocks:
if <statement is true>:
    <do something>
    ....
    ....
elif <another statement is true>: # else if
    <do something else>
    ....
    ....
else:
    <do another thing>
    ....
    ....
"""
x = 2
if x == 2:
    print "x equals two!"
else:
    print "x does not equal to two."

"""
Here are some examples for objects which are considered as empty: 
1. An empty string: "" 2. An empty list: [] 3. The number zero: 0 
4. The false boolean variable: False
"""

# Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. 
x = [1,2,3]
y = [1,2,3]
print x == y 	# Prints out True
print x is y 	# Prints out False


print not False 				# Prints out True
print (not False) == (False) 	# Prints out False


"""
### EXERCISE

Change the variables in the first section, so that each if statement resolves as True.
"""
print "\n### EXERCISE"
# Change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print "1"

if first_array:
    print "2"

if len(second_array) == 2:
    print "3"

if len(first_array) + len(second_array) == 5:
    print "4"

if first_array and first_array[0] == 1:
    print "5"

if not second_number:
    print "6"

