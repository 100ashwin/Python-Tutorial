# Python Function Docstrings

# Python provides a built-in function called help() that allows you to show the
# documentation of a function.

# help(print)

# Note that you can use the help() function to show the documentation of
# modules, classes, functions, and keywords

# Using docstrings to document functions

# When the first line in the function body is a string, Python will
# interpret it as a docstring.

def add(a, b):
    "Return the sum of two arguments"
    return a + b


help(add)
# output:
# Help on function add in module __main__:

# add(a, b)
#     Return the sum of two arguments


# Typically, you use multi-line docstrings:

def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b


help(add)
# output
# Help on function add in module __main__:

# add(a, b)
#     Add two arguments
#     Arguments:
#         a: an integer
#         b: an integer
#     Returns:
#         The sum of the two arguments


# Python stores the docstrings in the __doc__ property of the function.

print(add.__doc__)
# output:
# Add two arguments
# Arguments:
#     a: an integer
#     b: an integer
# Returns:
#     The sum of the two arguments


# Use the help() function to get the documentation of a function.
# Place a string, either single-line or multi-line strings, as the first line in
# the function to add documentation to it.
