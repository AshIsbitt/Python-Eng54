age = 19
driver_lisence = True


# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!

functs = ['vote and drive', 'vote', 'drive', 'drink']
user_input = ""

while True:
    user_input = input("\nPick a number, or exit: ")

    if user_input == "exit":
        print("goodbye")
        break
    elif int(user_input) == 0:
        if age >= 18 and driver_lisence == True:
            print("You can vote and drive")
        else:
            continue
    elif int(user_input) == 1:
        print("1")
        if age >= 18:
            print("You can vote")
        else:
            print("You can't drive")
            continue
    elif int(user_input) == 2:
        if driver_lisence:
            print("You can drive")
        else:
            print("Your too young to drive")
    elif int(user_input) == 3:
        if age >= 16:
            print("You can't drink in a pub, but someone can still get you a drink. Sneaky")