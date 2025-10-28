# Python continue

# The continue statement is used inside a for loop or a while loop.
# The continue statement skips the current iteration and starts the next one.

# Typically, you use the continue statement with an if statement to skip the
# current iteration once a condition is True.


# The following example shows how to use the for loop to display even
# numbers from 0 to 9:
for index in range(10):
    if index % 2:
        continue
    print(index)
# 0
# 2
# 4
# 6
# 8

# First, iterate over a range of numbers from 0 to 9 using a for loop with the
# range() function.
# Second, if the index is an odd number, skip the current iteration and start a
# new one. Note that the index % 2 returns 1 if the index is an odd number and 0
# if the index is an even number.


# The following example shows how to use the continue statement to display odd
# numbers between 0 and 9 to the screen:
counter = 0
while counter < 10:
    counter += 1

    if not counter % 2:
        continue

    print(counter)
# 1
# 3
# 5
# 7
# 9

# Use the Python continue statement to skip the current iteration and start
# the next one.
