"""
Modules in Python are simply Python files with the .py extension, 
which implement a set of functions. Modules are imported from other modules 
using the import command.

To import a module, we use the import command. Check out the full list 
of built-in modules in the Python standard library here: 
http://docs.python.org/2/library/

The first time a module is loaded into a running Python script, 
it is initialized by executing the code in the module once. 
If another module in your code imports the same module again, 
it will not be loaded twice but once only - so local variables 
inside the module act as a "singleton" - they are initialized only once.

http://www.learnpython.org/en/Modules_and_Packages
"""

### EXAMPLES

def do_the_examples():
	print "### EXAMPLES"
	import urllib
	import foo.bar			# Way 1
	from foo import bar		# Way 2

	print dir(urllib)
	# help(urllib)			# General help
	# help(urllib.urlopen)	# Help for specific function


"""
### EXERCISE

In this exercise, you will need to print an alphabetically sorted list 
of all functions in the re module, which contain the word find.
"""
def do_the_exercise():
	print "\n### EXERCISE"
	import re

	# Your code goes here
	find_members = []
	for member in dir(re):
	    if "find" in member:
	        find_members.append(member)

	print sorted(find_members)


do_the_examples()
do_the_exercise()
