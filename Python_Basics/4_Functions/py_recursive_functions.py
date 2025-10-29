# Python Recursive Functions

# A recursive function is a function that calls itself until it doesn’t.

# Additionally, a recursive function needs to have a condition to stop calling
# itself. So you need to add an if statement

# syntax:
# def f():
#     if condition:
#         # stop calling itself
#     else:
#         f() # calling itself

# If you don't add stop statement, it will run indefinitely.

# Typically, you use a recursive function to divide a big problem that’s difficult
# to solve into smaller problems that are easier to solve.

# examples:

def count_down(start):
    """ Count down from a number """
    print(start)

    next = start - 1
    if next > 0:
        count_down(next)


count_down(3)
# 3
# 2
# 1

# Using a recursive function to calculate the sum of a sequence.

# normal function without recursion


def sum(n):
    total = 0
    for index in range(n + 1):
        total += index

    return total


result = sum(100)
print(result)       # 5050

# with recursion
# using ternary operator, more concise


def re_sum(n):
    return n + re_sum(n - 1) if n > 0 else 0
# logic here is 100 + 99 + 98.....


result = sum(100)
print(result)       # 5050

# A recursive function is a function that calls itself until it doesn’t.
# And a recursive function always has a condition that stops calling itself.
