#Functions

def name_of_function(arg1, arg2):
    var = "hi"
    return var


#print(name_of_function(1,2))

def say_hello_zeus():
    return 'Hello Zeus'

print(say_hello_zeus())

def full_name_formatter(fname, lname):
    return fname.strip().capitalize() + ' ' + lname.strip().capitalize()

print(full_name_formatter("john", 'smith'))

def add_funct(num1, num2):
    return num1 + num2