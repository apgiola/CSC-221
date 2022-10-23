#Write a program that first gets a list of integers from input. 
#The input begins with an integer indicating the number of integers that follow. 
#Then, get the last value from the input, which indicates a threshold. 
#Output all integers less than or equal to that last threshold value.

def numList(user_values, upper_threshold): #create function to print values inside of threshold and a comma
    for value in user_values: #for loop creating variable value 
        if value <= upper_threshold: #if value is greater than or equal to the upper threshold
            print(value, end=',') #prints value
def getUserValues(): #user will enter their values here
    num = int(input()) #this will be first value entered, how many values will be accepted? 
    lst = [] #create blank list
    for i in range(num): #number of values accepted is amount iterated. 
        lst.append(int(input())) #add new values into the list until done with number of input values 
    return lst #returns list
if __name__ == '__main__': #will always run lol
    user_values = getUserValues() #user_values is assigned as the output of getUserValues function
    upper_threshold = int(input()) #our upper threshold which will be taken at end of all user values.
    numList(user_values, upper_threshold) #will print output.