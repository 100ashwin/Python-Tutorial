# Comments
# In python, a single-line comment begins with a hash(#) symbol followed by the comment.
# This is a single line comment in Python.


# Whitespace and indentation
# Python uses whitespace and indentation to construct the code structure.


# Continuation of statements
# Python uses a newline character to separate statements. It places each statement on one line.
# However, a long statement can span multiple lines by using the blackslash (\) character.


# Identifiers
# Identifiers are names that identify variables, functions, modules, classes, and other objects in Python.
# You cannot use Python keywords for namming identifiers.


# Keywords
# Some words have special meanings in Python. They are called keywords.
# Python provides a spcial module for listing its keywords called keyword.
import keyword
print(keyword.kwlist)   # list all the keywords in python
print("\n\n")           # line space


# String literals
# Python uses single quotes (''), double quotes (""), triple single quotes (''') and triple-double quotes (""") to denote a single literal.
s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line'''
print(s)
