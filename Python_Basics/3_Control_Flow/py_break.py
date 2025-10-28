# Python break

# Sometimes, you want to terminate a for loop or a while loop prematurely
# regardless of the results of the conditional tests. In these cases, you can
# use the break statement:

# Typically, you use the break statement with the if statement to terminate a
# loop when a condition is True.

# example
for index in range(0, 10):
    print(index)
    if index == 3:
        break
# 0
# 1
# 2
# 3

# When you use the break statement in a nested loop, it’ll terminate the
# innermost loop.
for x in range(3):
    for y in range(3):
        # terminate the innermost loop
        if y > 1:
            break
        # show coordinates on the screen
        print(f"({x}, {y})")
# (0, 0)
# (0, 1)
# (1, 0)
# (1, 1)
# (2, 0)
# (2, 1)


# The following shows how to use the break statement inside the while loop:
# The program will stop once you enter quit:
print('-- Help: type quit to exit --')
while True:
    color = input('Enter your favorite color: ')
    if color.lower() == 'quit':
        break

# Use the Python break statement to terminate a for loop or a while
# loop prematurely.
