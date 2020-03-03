import random

magic_number = random.randint(1, 10)
my_num = 0

while my_num != magic_number:
    my_num = int(input("Guess a number between 1 and 10 "))

    if my_num == magic_number:
        break

print("Thanks for playing")