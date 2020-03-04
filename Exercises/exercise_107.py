#1
# AS a User I want to be able to see the menu in a formatted way,
# so that I can order my meal.

# introduction text
print("Welcome to the cafe Python")
print("--------------------------")
print("Please see our menu here:\n")

# define menu
meal = ["BurGer", "PiZZa", "CHIps", "KebaB", "NuGGets",
        "ApplepIE", "IcecreAM", "CaKe"]

# for each item in the menu, print it's index and formatted text
for i in range(len(meal)):
    print("{}, {}".format(i, meal[i].capitalize()))

#2
# AS a User I want to be able to order 3 times, and have my responses added
# to a list so they aren't forgotten

# store customer order
order = []

# runs through the code until the user has ordered 3 items
while len(order) < 3:
    # data entry
    order_item = input("\nMay I take your order please?\nEnter an index value or item name. Type 'cancel' to exit: ")

    # if the user enters a number, convert to int and add relevant item to customer order list
    try:
        order_item = int(order_item)
        order.append(meal[order_item])
    # if user hasn't entered a number, ValueError will trigger
    except ValueError:
        # If user wants to cancel, break out of the code
        if order_item.lower() == "cancel":
            print("Thank you, come again")
            exit()
        # otherwise, if item is in the meal list, add to order list
        elif order_item.capitalize() in meal:
            order.append(order_item.capitalize())
        # if option not in the menu, ask them to try again
        else:
            print("Invalid option. Try again. (1)")
    # If user enters a number beyond the length of the menu list, IndexError will trigger
    except IndexError:
        print("Invalid option. Try again. (2)")

# Line break in the console
print("-----------------------------")

#3
# As a user, I want to have my order read back to me in formatted way so I know
# what I ordered.

# list through each item in the user's order and return the formatted item
print("Your order is:")
for i in range(len(order)):
    print("{}".format(meal[i].capitalize()))

# context printing
print("\nThat will come to...")
print("...")
print("Error. No price calculated")
print("Your order will be free")
