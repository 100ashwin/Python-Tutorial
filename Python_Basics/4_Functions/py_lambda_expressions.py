# Python Lambda Expressions

# Python lambda expressions allow you to define anonymous functions.

# Anonymous functions are functions without names. The anonymous functions
# are useful when you need to use them once.

# A lambda expression typically contains one or more arguments, but it can have
# only one expression.

# syntax:
# lambda parameters: expression

# In Python, you can pass a function to another function or return a function
# from another function.

# example:

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


def first_last(first_name, last_name):
    return f"{first_name} {last_name}"


def last_first(first_name, last_name):
    return f"{last_name} {first_name}"


full_name1 = get_full_name("John", "Doe", first_last)   # passing function as
full_name2 = get_full_name("Jane", "Doe", last_first)   # argument

print(full_name1)       # John Doe
print(full_name2)       # Doe Jane


# Instead of defining the first_last and last_first functions, you can use
# lambda expressions.

# example syntax:
# lambda first_name, last_name: f"{first_name} {last_name}"

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


# for first and last
full_name1 = get_full_name(
    "John",
    "Doe",
    lambda first_name, last_name: f"{first_name} {last_name}"
)

# for last and first
full_name2 = get_full_name(
    "John",
    "Doe",
    lambda first_name, last_name: f"{last_name}, {first_name}"
)

print(full_name1)       # John Doe
print(full_name2)       # Doe, John

# examples:


def times(n):
    return lambda x: x * n


square = times(4)       # here it defines the x value as 4
print(square)           # it will print function address not the answer

result = square(2)      # here the x value is 4
print(result)           # 8 -- 4 * 2

result = square(4)      # x value is 4
print(result)           # 16 -- 4 * 4


# Python lambda is loop
callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())
# 1
# 2
# 3

# Use Python lambda expressions to create anonymous functions, which are
# functions without names.

# A lambda expression accepts one or more arguments, contains an expression,
# and returns the result of that expression.

# Use lambda expressions to pass anonymous functions to a function and return a
# function from another function.
