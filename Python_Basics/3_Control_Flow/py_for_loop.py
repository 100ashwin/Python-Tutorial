# Python for loop with Range

# In programming, you often want to execute a block of code multiple times.
# To do so, you use a for loop.

# syntax:
# for index in range(n):
#     statement

# example:
for index in range(5):
    print(index)
# 0
# 1
# 2
# 3
# 4

for index in range(5):
    print(index + 1)
# 1
# 2
# 3
# 4
# 5

for index in range(1, 6):
    print(index)
# 1
# 2
# 3
# 4
# 5

for index in range(0, 11, 2):
    print(index)
# 0
# 2
# 4
# 6
# 8
# 10

# Calculate the sum of numbers from 1 to 100:
sum = 0
for num in range(101):
    sum += num

print(sum)          # 5050

n = 100
sum = n * (n + 1)/2
print(sum)          # 5050.0


# Use the for loop statement to run a code block a fixed number of times.
# Use the range(start, stop, step) to customize the loop.
