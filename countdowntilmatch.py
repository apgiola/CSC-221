# Program that takes in an integer in the range 11-100 as input. The output is a countdown starting 
# from the integer, and stopping when both output digits are identical. 

# Get integer between 11-100 from user
num = int(input())
# if value < 11 or > 100
if num < 11 or num > 100:
    print('Input must be 11-100') #input validation
else:
    digits_equal = False #set it 
    while digits_equal == False: #yep
        print(num) #print current num
        tens_value = (num % 100) // 10 #tens
        ones_value = num % 10 #ones
        if tens_value == ones_value: 
            digits_equal = True #end of iteration
        num -= 1 #decrement num