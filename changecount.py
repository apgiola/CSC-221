import math
#Int change amt from user
change_amt = int(input())
#If user inputs 0 change, pass No change to output
if change_amt < 1:
    print("No change")
#Number values of coins
dollar_val = 100
penny_val = 1
nickel_val = 5
dime_val = 10
quarter_val = 25

#start while loop if change_amt is greater than  0
while change_amt > 0:
    #first check if change_amt is greater than coin values
    if change_amt >= dollar_val:
        dollars = math.floor(change_amt / dollar_val)
        change_amt -= dollars * dollar_val
        if dollars > 1:
            print(dollars, "Dollars")
        else:
            print(dollars, "Dollar")
    #branch 2 for quarters
    elif change_amt >= quarter_val:
        quarters = math.floor(change_amt / quarter_val)
        change_amt -= quarters * quarter_val
        if quarters > 1:
            print(quarters, "Quarters")
        else:
            print(quarters, "Quarter")
    #branch 3 for dimes
    elif change_amt >= dime_val:
        dimes = math.floor(change_amt / dime_val)
        change_amt -= dimes * dime_val
        if dimes > 1:
            print(dimes, "Dimes")
        else:
            print(dimes, "Dime")
    #branch 4 for nickels
    elif change_amt >= nickel_val:
        nickels = math.floor(change_amt / nickel_val)
        change_amt -= nickels * nickel_val
        if nickels > 1:
            print(nickels, "Nickels")
        else:
            print(nickels, "Nickel")
    #branch 5 for pennies
    elif change_amt >= penny_val:
        pennies = math.floor(change_amt / penny_val)
        change_amt -= pennies * penny_val
        if pennies > 1:
            print(pennies, "Pennies")
        else:
            print(pennies, "Penny")
