# Python if-else statements

# if statement
age = input("Enter your age: ")
if int(age) >= 18:
    print("You're eligible to vote.")
# if age is greater than or equal to 18, it will execute the print() function.


# if-else statement
age = input("Enter your age: ")
if int(age) >= 18:
    print("You're eligible to vote.")
else:
    print("You're not eligible to vote.")
# if the age is not greater than 18, it will execute the else block.


# if-elif-else statement
age = input("Enter your age: ")

your_age = int(age)
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18

print(f"You'll pay ${ticket_price} for the ticket.")


# Use the if statement when you want to run a code block based on a condition.
# Use the if...else statement when you want to run another code block if the
# condition is not True.
# Use the if...elif...else statement when you want to check multiple conditions
# and run the corresponding code block that follows the condition that evaluates
# to True.
