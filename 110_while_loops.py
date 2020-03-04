c = 0
c = 0

while c <= 10:
    print(c)
    c += 1

#user_input = input('You want to play? ')

# while user_input == 'yes' or user_input == 'y':
#     random_num = 10
#     print('Welcome to our random game')
#     user_input = input('what is your guess ')
#     if user_input == random_num:
#         print("Correct")
#     else:
#         print('Try again')

while True:
    user_input = int(input("choose 1 for pancakes, 2 for cake, 3 to exit"))

    if user_input == 1:
        print("pancake")
    elif user_input == 2:
        print("cake")
    elif user_input == 3:
        print("goodbye")
        break
    else:
        print("try entering another value")

