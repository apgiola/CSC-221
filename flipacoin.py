import random

# A function named coin_flip that returns "Heads" or "Tails" according to a random value 1 or 0. 
# Assume the value 1 represents "Heads" and 0 represents "Tails". 
def coin_flip():
    rand_int = random.randint(0,1)
    if rand_int == 0:
        return 'Tails'
    else:
        return 'Heads'
   # Generate rand_num 0 or 1
   # If rand_num == 0
        # return 'Tails'
    # Else
        # return 'Heads'

if __name__ == '__main__':
    random.seed(5)  # Unique seed
    number_of_flips = int(input())
    for i in range(number_of_flips):
        print(coin_flip())
    # Loop num_of_flips time
        # Call coin_flip() and print results