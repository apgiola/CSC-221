# Random guessing game- Generate a random number between 1 - 50, user must then guess this number. 
# if the number is high, the user must be told it is high, and if it is low then the user must be told it is low
# if the user guesses 0, the program will quit, and will run in perpetuity until the number is guessed or 
# 0 is entered. The program will tell the user how many times the number was guessed. At the end, the program
# will ask the user if they want to play again. 

import random
#generate a random number between 1 - 50
rand_num = random.randint(1, 50)
#counter variable
counter = 0 #counter variable
usr_num = rand_num % 2 + 3 # pre-define usr_num for while loop, modulo 2 of rand_num + 3 so never outside bounds of loop
#start the program loop now
while usr_num > 0 and usr_num < 51: # 0 < input < 51
    usr_num = int(input("Guess a number between 1 and 50, or 0 to quit\n")) #takes user input
    counter += 1 #increment counter
    if usr_num > rand_num and usr_num < 51: # prints higher than random number
        print("Too High!")
        print()
    if usr_num < rand_num and usr_num != 0: # prints lower than random number
        print("Too Low!")
        print()
    if usr_num == rand_num: # prints victory message
        print('Congratulations! You have guessed the random number in', counter, 'tries!') #includes number of attempts
        q_answer = input('Do you want to play again? Y/N\n')
        if q_answer == 'Y' or 'y':
            print('Ok! Good luck!')
            rand_num = random.randint(1, 50)
            usr_num = rand_num % 2 + 3
        if q_answer == 'N' or 'n':
            
            break #end loop
    
else: # exception handling + quit
    if usr_num == 0: # user has quit, receive quit msg
        print("You have quit the game")
        print()
        quit() #quit entire program to avoid input validation else. 
    print("The number you have guessed is not a valid number") #usr_num is not valid entry. 
    print()