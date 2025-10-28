# Python pass

# The pass statement is a statement that does nothing. It’s just a placeholder
# for the code that you’ll write in the future.

# When you run the code that contains a pass statement, the Python interpreter
# will treat the pass statement as a single statement. As a result, it doesn’t
# issue a syntax error.

# Technically, you can use the pass statement in many statement in Python.

counter = 1
max = 10
if counter <= max:
    counter += 1
else:
    pass


for i in range(1, 100):
    pass

# while condition:
#     pass


def fn():
    pass


class Stream:
    pass

# Use the Python pass statement to create a placeholder for the code that
# you’ll implement later.
