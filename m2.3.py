my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
while x < len(my_list):
    number = my_list[x]
    if my_list[x] > 0:
        print(my_list[x])
    elif my_list[x] == 0:
        pass
    else:
        break
    x += 1