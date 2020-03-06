from fuzzbuzz_functional import *

# from folder.file, import function
from fuzzbuzz_functional.fizzbuzz_functional import fizz

while True:
    user_num = input("Give me a number ")

    print_num = 1
    print_list = []

    if user_num == "e":
        break

    for x in range(int(user_num)):
        out = str(print_num)

        if fizz(print_num, 3):
            out += " fizz"

        if fizz(print_num, 5):
            out += " buzz"

        print_list.append(out)
        print_num += 1

    for i in print_list:
        print(i)

    print("-----")