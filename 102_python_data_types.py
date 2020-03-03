# strings - text and characters
    # defined with "" and ''

# Define and concatenate
string = "Hello" + ' ' + "world"

# check data type
datatype_of_book = type(string)

# concatenate through function overloading
name = 'Ash'
Welcome_text = 'Welcome to sparta'

print(Welcome_text + ' ' + name)

# interpolation - inserting a string inside another strong
print(f'Welcome to class 54, We are Contested Terrain - by {input("what is your name? ")}')

print("Welcome {} to class 54".format(name))

# Useful methods
long_string = "this is a super long string to experiment around with??    "
# remove trailing whitespace
print(long_string.strip())
print(long_string.lower())
print(long_string.upper())
print(long_string.capitalize())
print(long_string.replace('?', '!'))

print("MULTIPLE METHODS")
ls = (long_string. strip().capitalize())
print(ls)

print(long_string.split())
