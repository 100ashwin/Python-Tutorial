# Python Functions

# A function is a named code block that performs a job or returns a value.

# Defining a Python Function
# Function definition
def greet():
    """ Display a greeting to users """
    print("Hi")


# Calling a Function
greet()             # Hi


# Passing information to Python Functions
def greet(name):
    print(f"Hi {name}")


greet('John')       # Hi John
first_name = "Jane"
greet(first_name)   # Hi Jane

# A parameter is a piece of information that a function needs. And you specify
# the parameter in the function definition.

# An argument is a piece of data that you pass into the function.

# Returning a value


def hello(name):
    return f"Hello {name}"


greeting = hello('Sam')
print(greeting)     # Hello Sam


# python functions with multiple parameters
# A function can have zero, one, or multiple parameters.
def sum(a, b):
    return a + b


total = sum(10, 20)
print(total)        # 30


# A Python function is a reusable named block of code that performs a task or
# returns a value.

# Use the def keyword to define a new function. A function consists of function
# definition and body.

# A function can have zero or more parameters. If a function has one or more
# parameters, you need to pass the same number of arguments into it.

# A function can perform a job or return a value. Use the return statement to
# return a value from a function.
