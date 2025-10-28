# Python Arithmetic Operators

# You use arithmetic operators to perform mathematicl operations on numbers.

x = 5
y = 2

# addition
print(x + y)                # 7
# subtraction
print(x - y)                # 3
# Multiplication
print(x * y)                # 10
# Division (Floating)
print(x / y)                # 2.5
# Floor Division
print(x // y)               # 2
# Modulus (Remainder)
print(x % y)                # 1
# Exponentiation
print(x ** y)               # 25


# You can use the modulus operator to check if a number is odd/even.
a = 101
if a % 2 == 1:
    print(f"{a} is odd.")
else:
    print(f"{a} is even.")
# 101 is odd.


# You can also use the % operator to check whether a year is a leap year or not.
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
# 2024 is a leap year.


# You can use the exponentiation operator to calculate the compound interest.
principal = 1000
interest_rate = 0.05
year = 2
amount = principal * (1 + interest_rate) ** year

print(f"Total Amount: ${amount:,.2f}")
