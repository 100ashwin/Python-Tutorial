# Python Ternary Operator

# example
age = 19
if age >= 18:
    ticket_price = 20
else:
    ticket_price = 5

print(f"The ticket price is ${ticket_price}")
# The ticket price is $20

# example with ternary operator -- to make it more concise.
ticket_price = 20 if age >= 18 else 5
print(f"The ticket price is ${ticket_price}")
# The ticket price is $20


# syntax:
# value_if_true if condition else value_if_false

# Use the ternary operator to make your code more concise.


# Note that you have been programming languages such as C# or Java, and you’re
# familiar with the following ternary operator syntax:

# condition ? value_if_true : value_if_false

# However, Python doesn’t support this kind of ternary operator syntax.
