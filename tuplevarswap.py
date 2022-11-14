# Define your function here.
def swap_values(user_val1, user_val2, user_val3, user_val4):
    temp1 = user_val1
    temp2 = user_val2
    temp3 = user_val3
    temp4 = user_val4
    user_val1 = temp2
    user_val2 = temp1
    user_val3 = temp4
    user_val4 = temp3
    global nums
    nums = (user_val1, user_val2, user_val3, user_val4)
    return nums
if __name__ == '__main__': 
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    swap_values(num1, num2, num3, num4)
    (out1, out2, out3, out4) = nums
    print(out1, out2, out3, out4)
    