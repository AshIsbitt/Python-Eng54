user_num = input("Give me a number ")
print_num = 1
print_list = []

for x in range(int(user_num)):
    out = str(print_num)
    if print_num % 3 == 0:
        out += "boring"
    if print_num % 5 == 0:
        out += "buzz"

    print_list.append(out)
    print_num += 1

print(print_list)