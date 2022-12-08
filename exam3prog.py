# Anthony Giola
# CSC 221 
# 12/7/22
# Professor Scott Davis / Tidewater Community College
# 1 - Modify main program to read five integers from the 
# user into an array/list. Sort the integers into ascending value and print out the values.
def calc_score(input_list):
    x = sum(input_list)
    print(f'Total: {x}')
    return x
    


def count_sixes(input_list2):
    counter = 0
    for i in input_list2:
        if i == 6:
            counter += 1
    print(f'Sixes: {counter}')

            


if __name__ == '__main__':  # Do not modify this line
    val_five_list = []
    while len(val_five_list) < 5:
        usr_vals = input()
        usr_vals2 = usr_vals.split()
        for i in range(0, len(usr_vals2)):
            usr_vals2[i] = int(usr_vals2[i])
        val_five_list = usr_vals2
    val_five_list.sort()
    for i in range(0, len(val_five_list)):
        print(val_five_list[i], end=' ')

    
    print();calc_score(val_five_list)
    
    
    count_sixes(val_five_list)