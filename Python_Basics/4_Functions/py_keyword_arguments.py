# Python Keyword Arguments

# example
def get_net_price(price, discount):
    return price * (1 - discount)


net_price1 = get_net_price(100, 0.1)
net_price2 = get_net_price(0.1, 100)

print(net_price1)       # 90.0
print(net_price2)       # -9.9

# here the python doesn't know which argument is which, that's why the answer
# are different, to solve this, we use keyword arguments.

net_price3 = get_net_price(
    price=100,
    discount=0.1
)
# or
net_price4 = get_net_price(
    discount=0.1,
    price=100
)

print(net_price3)       # 90.0
print(net_price4)       # 90.0

net_price5 = get_net_price(
    100,
    discount=0.1
)
print(net_price5)       # 90.0


# Keyword arguments and default parameters
def another_net_price(price, tax_rate=0.07, discount=0.05):
    discount_price = price * (1 - discount)
    net_price = discount_price * (1 + tax_rate)

    return net_price

# In the another_net_price() function, the tax and discount parameters have
# default values of 7% and 5% respectively.


new_price = another_net_price(100)
print(f"{new_price:.2f}")       # 101.65

# Once you use a keyword argument, you need to use keyword arguments for the
# remaining parameters.
# example

# new_price1 = another_net_price(
#     100,
#     tax = 0.08,
#     0.06
# )    # this will give error

# instead use, keyword arguement
new_price1 = another_net_price(
    100,
    tax_rate=0.08,
    discount=0.06
)
print(f'{new_price1:.2f}')   # 101.52


# Use the Python keyword arguments to make your function call more readable
# and obvious, especially for functions that accept many arguments.

# All the arguments after the first keyword argument must also be keyword
# arguments too.
