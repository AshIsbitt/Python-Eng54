# Practice String
# Exercise 1

#Define a string var
user_name = ""

# prompt user for input and set to original var
user_name = input("What is your name? ")

#output a welcome message using formatted strings
print("Welcome {}, you are in the Sparta zone".format(user_name.strip()))

#ask the user for their first and last name in different vars
firstname = input("What is your first name? ")
lastname = input("What is your last name? ")

#output data using a different formatting method
print(f"Welcome to Sparta training, {firstname + lastname}!")

# Exercise 2
