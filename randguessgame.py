# Random guessing game- Generate a random number between 1 - 50, user must then guess this number. 
# if the number is high, the user must be told it is high, and if it is low then the user must be told it is low
# if the user guesses 0, the program will quit, and will run in perpetuity until the number is guessed or 
# 0 is entered. The program will tell the user how many times the number was guessed. At the end, the program
# will ask the user if they want to play again. 

import random
from urllib.parse import uses_fragment
#generate a random number between 1 - 50
rand_num = random.randint(1, 50)

#start the program loop now
while usr_num > 0 and usr_num <:
    usr_num = int(input())
    if usr_num > rand_num:
        print("You have guessed a number higher than the random number")
    if usr_num < rand_num:
        print("You have guessed a number lower than the random number")
    if usr_num == rand_num:
        print("Congratulations! You have guessed the random number")
        break