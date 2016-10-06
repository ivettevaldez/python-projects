"""
Objects are an encapsulation of variables and functions into a single entity. 
Objects get their variables and functions from classes. 
Classes are essentially a template to create your objects.

http://www.learnpython.org/en/Classes_and_Objects
"""

### EXAMPLES
class MyClass:
	variable = "blah"

	def function(self):
		print "This is a message inside the class."

def do_the_examples():
	print "### EXAMPLES"
	myobjectx = MyClass()
	print myobjectx.variable   # This would print "blah".

	myobjecty = MyClass()
	myobjecty.variable = "yackity"

	print myobjectx.variable   # This would print "blah".
	print myobjecty.variable   # This would print "yackity".

	myobjectx.function()	   # This would print out the message: "This is a message inside the class."


"""
### EXERCISE

We have a class defined for vehicles. Create two new vehicles called car1 and car2. 
Set car1 to be a red convertible worth $60,000 with a name of Fer, 
and car2 to be a blue van named Jump worth $10,000.
"""

# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

def do_the_exercise():
	# Your code goes here
	car1 = Vehicle()
	car1.color = "red"
	car1.kind = "convertible"
	car1.value = 60000
	car1.name = "Fer"

	car2 = Vehicle()
	car2.color = "blue"
	car2.kind = "van"
	car2.value = 10000
	car2.name = "Jump"

	# Test code
	print "\n### EXERCISE"
	print car1.description()
	print car2.description()


do_the_examples()
do_the_exercise()
