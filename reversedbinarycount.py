import math
usr_num = int(input())
#take user input

#loop as long as usr_num is > 0
while usr_num > 0:
    print(usr_num % 2, end='')
    usr_num = math.floor(usr_num / 2)
print()