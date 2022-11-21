import math
usr_input = input()
my_list = usr_input.split()

if len(my_list) > 9:
    print("Too many inputs")
else:
    num = math.floor((len(my_list) - 1 )/ 2)
    print(my_list[num])