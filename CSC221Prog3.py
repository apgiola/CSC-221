# Anthony Giola
# 11/26/22
# CSC 221 - Professor Scott Davis, Tidewater Community College
# Program 3 Psuedo Code
# Your program should calculate how many values in a list of randomly generated integers are odd and 
# how many are even with the following requirements:
# Get the number of values to be generated along with the range of values from the user. 
# After calculating the total number of odd and even values, display the results and allow the user to 
# continue to generate and count new sets of values until they choose to exit.

# import random
# define function that gets input values.
    # Get number of desired values from user input
    # Get range of desired values from user input
    # return 2 values

# define list function with number of values, and range of desired values as arguments
    # create blank list variable
    # for loop with with number of values
        # append to blank list variable a variable with desired range of values
    # return finished list

# define function to count the number of negative/postitive values. list is argument
    # negative count = 0
    # positive count = 0
    # for loop of length of list variable
        # if value[i] % 2 != 0 then 
            # negative count += 1
        # if value[i] % 2 == 0 then
            # positive count += 1
    # positive percentage = positive count / length of finished list
    # negative percentage = negative count / length of finished list
    # print positive percentage
    # print negative percentage

# body if then statement is executed
    # asign variable to call list function with input value function returns as arguments
    # list variable as argument to neg/pos value function. Will print percentages
    # new yes / no input question
    # if user selects yes
        # while user_selection variable is Y 
            # asign variable to call list function with input value function returns as arguments
            # list variable as argument to neg/pos value function. Will print percentages
            # new yes / no input question
        # else
            # quit program.
        
