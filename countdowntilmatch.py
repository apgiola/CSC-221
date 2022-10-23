# Program that takes in an integer in the range 11-100 as input. The output is a countdown starting 
# from the integer, and stopping when both output digits are identical. 

# Get integer between 11-100 from user
num = int(input())

# if value < 11 or > 100
if num < 11 or num > 100:
    print('Input must be 11-100')
else:
    digits_equal = False
    while digits_equal == False:
        print(num)
        tens_value = (num % 100) // 10
        ones_value = num % 10
        if tens_value == ones_value:
            digits_equal = True
        num -= 1