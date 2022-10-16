number = 1
while number > 0:
    usr_num = int(input())
    if usr_num > number:
        number = usr_num
    if usr_num == 0:
        number = usr_num
        break
    if usr_num < 0:
        break
print(number)