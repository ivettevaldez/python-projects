"""
Generators are used to create iterators, but with a different approach. 
Generators are simple functions which return an iterable set of items, 
one at a time, in a special way.

When an iteration over a set of item starts using the for statement, 
the generator is run. Once the generator's function code reaches a 
"yield" statement, the generator yields its execution back to the for loop, 
returning a new value from the set. The generator function can generate 
as many values (possibly infinite) as it wants, yielding each one in its turn.

http://www.learnpython.org/en/Generators
"""

### EXAMPLES

print "### EXAMPLES"
"""
This function decides how to generate the random numbers on its own, 
and executes the yield statements one at a time, pausing in between 
to yield execution back to the main for loop.

Generator function which returns 7 random integers:
"""
import random

def lottery():
    # Returns 6 numbers between 1 and 40
    for i in xrange(6):
        yield random.randint(1, 40)

    # Returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
    print "And the next number is... %d!" % random_number


"""
### EXERCISE

Write a generator function which returns the Fibonacci series. 
They are calculated using the following formula: 
The first two numbers of the series is always equal to 1, 
and each consecutive number returned is the sum of the last two numbers. 

Hint: Can you use only two variables in the generator function? 
Remember that assignments can be done simultaneously. 
"""
# Will simultaneously switch the values of a and b.
a = 1
b = 2
a, b = b, a
print "a equals %d and b equals %d" % (a, b)

print "\n### EXERCISE"
# Fill in this function
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

# Testing code
import types
if type(fib()) == types.GeneratorType:
    print "Good, The fib function is a generator."

    counter = 0
    for n in fib():
        print n
        counter += 1
        if counter == 10:
            break


