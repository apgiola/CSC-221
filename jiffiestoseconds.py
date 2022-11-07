# A function named jiffies_to_seconds that takes the number of "jiffies" as a parameter, 
# and returns the number of seconds.
def jiffies_to_seconds(user_jiffies):
    seconds = user_jiffies / 100
    return seconds

if __name__ == '__main__':
    user_jiffies = float(input())
    seconds = jiffies_to_seconds(user_jiffies)
    print(f'{seconds:.3f}')