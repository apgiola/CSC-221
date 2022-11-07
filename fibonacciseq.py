# Function, which has an index n as parameter and returns the nth value in the fibonacci sequence. 
# Any negative index values should return -1.
# The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, 
#           ex: 0, 1, 1, 2, 3, 5, 8, 13
from math import sqrt
import math
def fibonacci(n): #function
    if n < 0:
        return -1
    elif n > 1:
        for i in range(n): #for loop to iterate until defined nth term of fibonacci sequence.
            sequence = ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)) # Fibonacci Sequence formula
            return math.floor(sequence)
    elif n == 0:
        return 0
    else: 
        return 1
if __name__ == '__main__': # main module
    start_num = int(input()) #usr input 
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}') #function call and print