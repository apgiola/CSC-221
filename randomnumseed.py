# Exercise 1: "Read a "seed" value from input and set the random number seed with that value. 
# Then get a value from the user that determines how many random numbers to generate. 
# Write a loop that will print out that many random numbers between 1 and 100."

# Get user seed input and place inside random number generator
import random
import statistics
seed_input = int(input())
random.seed(seed_input)

# Get user number of iteration input 
iter_input = int(input())
for i in range(iter_input): #range of iterations by user definition
    i = random.randint(1, 100) #random number between 1 and 100
    print(i) #print i



# Exercise 2: "Input positive integers until the user enters a negative number, 
# then calculate and print the average of those entered numbers.

# Get first user input
usr_input = float(input()) #first user input
lst = [usr_input] # include first user input
while usr_input >= 0: # if user enters positive number, this will
    usr_input = float(input()) #accept floats for grading
    if usr_input < 0: # we dislike negative numbers here
        break #kills loop if negative number is entered
    if usr_input >= 0: #accept positive number
        lst.append(usr_input) # looped input to list if above 0
if len(lst) != 0: # Average numbers as long as there is a single positive number
    average = sum(lst) / len(lst) #average with length of list and sum of all items in the list. 
else: # if they only entered negative numbers
    average = float(0)

print('Average:', f'{average:.2f}') # print usr_input average)



# Exercise 3: "Based on the average from #2, print out a grade where 90 or higher 
# is an 'A', 80 to 90 is a 'B', 70 to 80 is a 'C', 60 to 70 is a 'D' and under 60 is an 'F'."

# acceptable range
if average == type(float) or type(int): # if-elif-else statement for grade
    if average < 60:
        print('Grade: F')
    elif average < 70:
        print('Grade: D')
    elif average < 80:
        print('Grade: C')
    elif average < 90:
        print('Grade: B')
    elif average <= 100:
        print('Grade: A')
    else: 
        print('You somehow broke the grade book! Contact your teacher.') #error message somehow? 

    