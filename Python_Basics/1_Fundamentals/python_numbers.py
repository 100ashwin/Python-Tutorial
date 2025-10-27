# Python supports integers, floats, and complex numbers.

# Integers
# The integers are numbers such as -1, 0, 1, 2, and 3, .. and they have type int.

# You can use Math operators like +, -, *, and / to form expressions that include integers.
x = 20
y = 10

print(x + y)        # 30
print(x - y)        # 10
print(x * y)        # 200
print(x / y)        # 2.0

# To calculate exponents, you use two multiplication symbols (**).
x = 3
y = 3
power = x ** y
print(power)        # 27

# To modify the order of operations, you use the parentheses ().
result = 20 / (10 + 10)
print(result)       # 1.0


# Floats
# Any number with a decimal point is a floating-point number. The term float means that the decimal point can appear at any position in a number.
# In general, you can use floats like integers.
x = 0.5
y = 0.25

print(x + y)        # 0.75
print(x - y)        # 0.25
print(x * y)        # 0.125
print(x / y)        # 2.0

# The division of two integers always returns a float
# If you mix an integer and a float in any arithmetic operation, the result is a float
x = 1
y = 2.0
print(x / y)        # 0.5

# When a number is large, it'll become difficult to read.
# To make the long numbers more readable, you can group digits using underscores
count = 10_000_000_000
print(count)        # 10000000000
# When storing these values, Python just ignores the underscores. It does so when displaying the numbers with underscores on the screen:


# complex
x = 7 + 8j
y = 7j
# j is imaginary part it is important
print(x)            # (7+8j)
print(y)            # 7j