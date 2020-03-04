
# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu

while True:
    user_num = input("Give me a number ")
    print_num = 1
    print_list = []

    if user_num == "penpinapplespen":
        break

    for x in range(int(user_num)):
        out = str(print_num)
        if print_num % 3 == 0:
            out += "bizz"
        if print_num % 5 == 0:
            out += "zzuu"

        print_list.append(out)
        print_num += 1

    print(print_list)