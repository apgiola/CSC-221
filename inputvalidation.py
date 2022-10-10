import re
usr_input = input("Type 'Input' here to play the game.")
if not re.match("^[a-zA-Z]+$", usr_input):
    print("Error: Invalid input")
    quit()
else: 
    while 'Input' in usr_input:
        print("You are amazing at following directions!")
        new_input = input("Type 'No' here to play the game.")
        usr_input = '0'
    while 'No' not in usr_input:
        print("You're either very disagreeable or you listened!")
        break
    