#1
# AS a User I want to be able to see the menu in a formatted way,
# so that I can order my meal.
print("Welcome to the cafe Python")
print("Please see our menu here:\n")

meal = ["Burger", "Pizza", "Chips", "Kebab", "Nuggets",
        "Applepie", "Icecream", "Cake"]

print(meal)

#2
# AS a User I want to be able to order 3 times, and have my responses added
# to a list so they aren't forgotten
order = []

while len(order) < 3:
    order_item = input("\nMay I take your order please?\nEnter an index value or item name. Type /'cancel/' to exit: ")

    try:
        order_item = int(order_item)
        order.append(meal[order_item])
    except ValueError:
        if order_item.lower() == "cancel":
            break
        elif order_item.capitalize() in meal:
            order.append(order_item.capitalize())
        else:
            print("Invalid option")

#3
# As a user, I want to have my order read back to me in formatted way so I know
# what I ordered.

print("Your order is {}".format(order))
print("That will come to...")
print("...")
print("Error. No price calculated")
print("Your order will be free")
