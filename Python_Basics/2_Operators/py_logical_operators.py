# Python Logical Operators
# Sometimes, you may want to check multiple conditions at the same time.
# To do so, you use logical operators.

# Python has three logical operators:

# and
# or
# not

# The and operator checks whether two conditions are both True simultaneously:
# It returns True if both conditions are True. And it returns False if either
# the condition a or b is False.

price = 9.99
result = price > 10 and price < 20
print(result)           # False


# Similar to the and operator, the or operator checks multiple conditions.
# But it returns True when either or both individual conditions are True:
# The or operator returns False only when both conditions are False.

price = 9.99
result = price > 10 or price < 20
print(result)           # True


# The not operator applies to one condition. And it reverses the result of
# that condition, True becomes False and False becomes True.
# If the condition is True, the not operator returns False and vice versa.

is_active = True
print(is_active)        # True
print(not (is_active))   # False

price = 9.99
result = not price > 10
print(result)           # True

price = 9.99
result = not (price > 5 and price < 10)
print(result)           # False


# Precedence of Logical Operators
# The precedence of the logical operator from the
# highest to lowest: not, and, and or.
