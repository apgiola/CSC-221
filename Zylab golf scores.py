''' Type your code here. '''
import math
#Int change amt from user
change_amt = int(input())
#Number values of coins
penny_val = 1
nickel_val = 5
dime_val = 10
quarter_val = 25

#start while loop if change_amt is greater than or equal to 0
while change_amt >= 0:
    #establish if any amount is divisible solely by 1 coin.
    if change_amt % quarter_val == 0:
        print(change_amt / quarter_val, 'Quarters')
        break
    elif change_amt % dime_val == 0:
        print(change_amt / dime_val, 'Dimes')
        break
    elif change_amt % nickel_val == 0:
        print(change_amt / nickel_val, 'Nickels')
        break
    else:
        #gives amount of quarters that will fit in change_amt
        quarters = math.floor(change_amt / quarter_val)
        #dimes are change_amt minus quarters times 25 divided by 10
        if change_amt % quarters != 0:
            dimes = math.floor((change_amt - (quarters * quarter_val)) / dime_val)
            
        #nickels are change_amt minus (quarters times 25) minus (dimes times 10) / 5
        nickels = math.floor((change_amt - (quarters * quarter_val) - (dimes * dime_val)) / 5)
        pennies = math.floor((change_amt - (quarters * quarter_val) - (dimes * dime_val) - (nickels * nickel_val)) / 1)
        print(quarters, dimes, nickels, pennies)
        if quarters > 1:
            print(quarters, "quarters")
        else:
            print(quarters, "Quarter")
        if dimes > 1:
            print(dimes, "Dimes")
        else:
            print(dimes, "Dime")
        if nickels > 
        break
    