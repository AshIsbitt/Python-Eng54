#get user age
user_age = input("How old are you? ")
#subtract user age from current year
year_of_birth = 2020 - int(user_age)
#return message
print("Oh cool {}, you are {} years old, and were born in {}".format(user_name, user_age,
                                                                     year_of_birth))