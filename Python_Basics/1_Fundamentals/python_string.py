# A string is a series of characters. In Python, anything inside quotes is a string.
# And you can use either single or double quotes.

message = 'This is a string in Python'
message = "This is also a string"

# If a string contains a single quote, you should place it in double-quotes like this:
message = "It's a string"

# And when a string contains double quotes, you can use the single quotes:
message = '"Beautiful is better than ugly.". Said Tim Peters'

# To escape the quotes, you can use the backslash (\). for example:
message = 'It\'s also a valid string'

# The Python interpreter will treat the backslash character (\) special.
# If you don't want it to do so, you can use raw strings by adding the letter r before the first quote.
message = r'C:\python\bin'

# To span a string multiple lines, you use triple-quotes
help_message = '''
Usage: mysql command
    -h hostname
    -d database name
    -u username
    -p password
'''
print(help_message)

# Using variables in Python strings with the f-sttrings
name = 'John'
message = f"Hi {name}"
print(message)      # Hi John

# Concatenating Python strings
greeting = "Good "
time = "Afternoon"
message = greeting + time + "!"
print(message)      # Good Afternoon!

# Accessing string elements
# Since a string is a sequence of characters, you can access its elements using an index.
# index starts with 0 (zero).
str = "Python String"
print(str[0])       # P
print(str[1])       # y
# If you use a negative index, Python returns the character starting from the end of the string.
print(str[-1])      # g
print(str[-2])      # n

# Getting the length of a string
# To get the length of a string, you use the len() function.
str = "Python String"
str_len = len(str)
print(str_len)      # 13   
print(len(str))     # 13


# Slicing strings
# Slicing allows you to get a substring from a string.
str = "Python String"
print(str[0:2])     # Py --> character from index 0 (included) to 2 (excluded)
# syntax
# string[start: end]
# string[start: end: step]
print(str[0:10:2])  # Pto t --> step value is 2 so 0, 2, 4, 8 index


# Python strings are immutable.
# It means that you cannot change the string.
str = "Python String"
# str[0] = 'J'      # will give error

# when you want to modify a string, you need to create a new one from the existing string.
new_str = "J" + str[1:]
print(new_str)      # Jython String

# Use f-string to embed variable within a string literal.
name = "Ashwin"
message = f"Hello, {name}"
print(message)      # Hello, Ashwin
