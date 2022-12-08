# Anthony Giola
# 12/4/22
# CSC 221 - Professor Scott Davis, Tidewater Community College
# Program 3 
# Your program should calculate how many values in a list of randomly generated integers are odd and 
# how many are even with the following requirements:
# Get the number of values to be generated along with the range of values from the user. 
# After calculating the total number of odd and even values, display the results and allow the user to 
# continue to generate and count new sets of values until they choose to exit.

# import random to gen
import random
# define function that gets input values.
def usr_inputval():
    # Get number of desired values from user input
    num_val = int(input("How many values do you want to generate?"))
    range_val = int(input("What is the range of values you want to generate 1 to )?"))
    # input validation handling inside function 
    while type(num_val) != int and type(range_val) != int: 
        # num_val validation
        while type(num_val) != int:
            print('You have entered an invalid value for number of generated values. Try again')
            num_val = int(input("How many values do you want to generate?"))
        #range_val validation
        while type(range_val) != int:
            print('You have entered an invalid value for range of generated values. Try again')
            range_val = int(input("What is the range of values you want to generate 1 to )?"))
    # all fields pass lets get a tuple with output! 
    else:
        two_val = range_val, num_val
        # output tuple two_val
        return two_val
            
# define list function with number of values, and range of desired values as arguments
def list_creation(num_val, range_val):
    # create blank list variable
    new_list = []
    # for loop with with number of values
    for i in range(num_val):
        # append to blank list variable a variable with desired range of values
        new_list.append(random.randint(1, range_val))
        # -- Testing print(len(new_list))
    # return finished list
    return new_list

# define function to count the number of negative/postitive values. list is argument
def count_values(input_list):
    # negative count = 0
    neg_count = 0
    # positive count = 0
    pos_count = 0
    # for loop of length of list variable
    for i in range(len(input_list)):
        # if value[i] % 2 != 0 then 
        if input_list[i] % 2 != 0:
            # negative count += 1
            neg_count += 1
        # if value[i] % 2 == 0 then
        elif input_list[i] % 2 == 0:
            # positive count += 1
            pos_count += 1
    # positive percentage = positive count / length of finished list
    pos_percent = pos_count * 100 / len(input_list)
    # negative percentage = negative count / length of finished list
    neg_percent = neg_count* 100 / len(input_list)
    # print negative percentage
    print(f'Odd Values: {neg_percent:.1f}%')
    # print positive percentage
    print(f'Positive Values: {pos_percent:.1f}%')

# body if then statement is executed
if __name__ == '__main__':
    # super value for main while loop for try/except statement
    super_val = True
    # main while loop for try/except statement
    while super_val == True:
        # program logic inside try
        try:
            user_sel = True
            # while loop to run program logic
            while user_sel == True:
                # create our tuple variable
                two_val = usr_inputval()
                # unpack that tuple we made
                (range_val, num_val) = two_val
                # create list from list function - arguments are from usr_inputval()
                finished_lst = list_creation(num_val, range_val)
                # we count values and output them. List is the argument
                count_values(finished_lst)
                # ask user to re-run program logic or quit program
                user_selection_input = input("Do you want to generate a new set of values? (Y/N)")
                # user says no! 
                if user_selection_input == 'n':
                    user_sel = False
                elif user_selection_input == 'N':
                    user_sel = False
                # user says yes!
                else:
                    print('lets play again!')
                    continue
            # bye bye message and end program
            else: 
                print('Thank you for playing the game!')
                super_val = False
        # user somehow messed up and earlier validation didn't catch it. Reruns program if an error is caught: IE - ValueError        
        except:
            print('you have entered an invalid value for the range or number of values to be generated! Try again!')
            continue
# just in case ? 
else: 
    print('Woops, I\'m broken!')