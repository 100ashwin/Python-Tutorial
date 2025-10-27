# In programming, you often want to check if a condition is true or not and
# perform some actions based on the result.
# To represent true and false, Python provides you with the boolean data type.
# The boolean value has a technical name as bool.

# The boolean data type has two values: True and False.

is_active = True
is_admin = False

# When you compare two numbers, Python returns the result as a boolean value.
x = 20
y = 10

print(x > y)        # True
print(x < y)        # False

# Also, comparing two strings results in a boolean value:
x = 'a'
y = 'b'

print(x > y)        # False
print(x < y)        # True


# The bool() function
# To Find out if a value is True or False, you use the bool() function.

result = bool("HI")
print(result)       # True

result = bool(100)
print(result)       # True

result = bool(0)
print(result)       # False


# Falsy and Truthy Values
# when a value evaluates to True, it's truthy. If a value evaluates to False,
# it's falsy.

# The following are falsy values in Python
# Flasy values are the number zero, an empty string, False, None,
# an empty list [], an empty tuple (), and an empty dictionary {}.

# The truthy values are the other values that aren't falsy.

# None, list, tuple, and dictionary -- later in the upcomming tutorials.
