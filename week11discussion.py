import random
#generate a function that assigns a random grade to your cruddy essay
def rand_essay_score(usr_input): #defines a function that uses one input from user.
    random.seed(usr_input) #takes input for random seed
    score = random.randint(50,100) #generates a random int from 50 - 100
    if score >= 90: # A
        print('Congrats, you got an A randomly!')
    elif score >= 80: # B
        print('Congrats, you got a B randomly!')
    elif score >= 70: # C
        print('Congrats, you got a C randomly!')
    elif score >= 60: # Damn D
        print('Wow, that sucks, you got a D randomly!')
    else: # Press F to pay respects
        print('Bad luck bro, thats an F!')

usr_input = int(input('Type a random number here!')) # user input!
print('Let\'s find out what your grade is...') # cool message 
rand_essay_score(usr_input) #output. 
