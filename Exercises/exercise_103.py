name = "Lana"
last_name = ""
species = ""
eye_color = ""
hair_color = ""

name = input("Choose a new first name ")
last_name = input("Choose a new last name ")
species = input("Choose a new species ")
eye_color = input("Choose a new eye colour ")
hair_color = input("Choose a new hair colour ")

print("Hi {} {}".format(name, last_name))
print("I love your {} hair! And your {} eyes are so piercing".format(hair_color, eye_color))
print("I love {}".format(species))