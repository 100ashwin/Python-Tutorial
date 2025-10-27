# Python Type Conversion

# To get input from users, you use the input() function.
value = input("Enter a value: ")            # 100
print(value)                                # 100

# However, the input() function returns a string, not an integer or any other
# data type.

# for example what if you want to perform operation on input values of integer
# so for that you can use int() function. or any other data type function
# which you need.
# for example:

price = input("Enter a price ($): ")        # 100
tax = input("Enter the tax rate (%): ")     # 10

tax_amount = int(price) * int(tax) / 100
print(f"The tax amount is ${tax_amount}")   # The tax amount is $10.0

# you can also use the type conversion on input() function
# for example: price = int(input(...))

# Other type conversion functions
# Besides the int(str) functions, Python supports other type conversion
# functions. The following shows the most important ones for now:

# float(str) – convert a string to a floating-point number.
# bool(val) – convert a value to a boolean value, either True or False.
# str(val) – return the string representation of a value.


# Getting the type of a value:
# To get the type of value, you use the type(value) function.
result_type = type(100)
print(result_type)      # <class 'int'>

print(type(2.0))        # <class 'float'>
print(type("Hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>


# Use the input() function to get an input string from users.
# Use type conversion functions such as int(), float(), bool(), and str(value)
# to convert a value from one type to another.
# Use the type() function to get the type of a value.
