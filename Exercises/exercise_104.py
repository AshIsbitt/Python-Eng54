import datetime

name = "Lana"
last_name = ""
species = ""
eye_color = ""
hair_color = ""

now = datetime.datetime.now()

name = input("Choose a new first name ")
last_name = input("Choose a new last name ")
species = input("Choose a new species ")
eye_color = input("Choose a new eye colour ")
hair_color = input("Choose a new hair colour ")
age = input("How old are you? ")

year_of_birth = now.year - int(age)

print("Hi {} {}".format(name, last_name))
print("I love your {} hair! And your {} eyes are so piercing".format(hair_color, eye_color))
print("I love {}".format(species))

print("You were born in {} because you are {} years old".format(year_of_birth, age))

mother_name = input("What's your mother's name ")
mother_age = input("How old is {} ".format(mother_name))

mother_birth = now.year - int(mother_age)

print("She was born in {}".format(mother_birth))
print("You were born when she was {} years old".format(int(mother_age)-int(age)))