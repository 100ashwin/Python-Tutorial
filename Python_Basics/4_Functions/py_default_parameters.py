# Python Default Parameters

# When you define a function, you can specify a default value for
# each parameter.

# When you call a function and pass an argument to the parameter that has a
# default value, the function will use that argument instead of the default value.

# However, if you don’t pass the argument, the function will use the default value.

def greet(name, message="Hi"):
    return f"{message}, {name}"


greet1 = greet("John", "Hello")
greet2 = greet("Jane")      # here we are not passing the argument for message.

print(greet1)       # Hello, John
print(greet2)       # Hi, Jane


# Multiple default parameters

def hello(name="there", message="Hi"):
    return f"{message} {name}"


hello1 = hello()
hello2 = hello("Sam", 'Welcome')
hello3 = hello('Jane')
hello4 = hello(message="Welcome")

print(hello1)       # Hi there
print(hello2)       # Welcome Sam
print(hello3)       # Hi Jane
print(hello4)       # Welcome there

# Use Python default parameters to simplify the function calls.
# Place default parameters after the non-default parameters.
