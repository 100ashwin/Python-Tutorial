# Python comparison Operators
# In programming, you often want to compare a value with another value.
# To do that, you use comparison operators.

# Python has six comparison operators:
# Less than ( < )
# Less than or equal to (<=)
# Greater than (>)
# Greater than or equal to (>=)
# Equal to ( == )
# Not equal to ( != )

# These comparison operators compare two values and return a boolean value,
# either True or False.

# You can use these comparison operators to compare both numbers and strings.

x = 10
y = 20

print(x < y)            # True
print(x > y)            # False
print(x <= y)           # True
print(x >= y)           # False
print(x == y)           # False
print(x != y)           # True

result = "apple" < "orange"
print(result)           # True

result = "banana" < 'apple'
print(result)           # False
