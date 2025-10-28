# Python While loop

# Python while statement allows you to execute a code block repeatedly as long
# as a condition is True.

# syntax:
# while condition:
#     body

# In the body of the loop, you need to do something to stop the loop at some time.

# The condition is an expression that evaluates to a boolean value,
# either True or False.

# while statement to show 5 numbers from 0 to 4 to the screen.
max = 5
counter = 0

while counter < max:
    print(counter)
    counter += 1
# 0
# 1
# 2
# 3
# 4

#  while statement to prompt users for input and echo the command that you
# entered back. It’ll run as long as you don’t enter the quit command:
command = ''

while command.lower() != 'quit':
    command = input('> ')
    print(f"Echo: {command}")
