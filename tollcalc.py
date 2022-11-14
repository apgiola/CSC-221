# Function that has three parameters: the current hour of time (int), whether the time is morning (boolean), 
# and whether the day is a weekend (boolean). 
# The function returns the correct toll fee (float), based on the chart:
'''
Weekday Tolls
    Before 7:00 am ($1.15)
    7:00 am to 9:59 am ($2.95)
    10:00 am to 2:59 pm ($1.90)
    3:00 pm to 7:59 pm ($3.95)
    Starting 8:00 pm ($1.40)
Weekend Tolls
    Before 7:00 am ($1.05)
    7:00 am to 7:59 pm ($2.15)
    Starting 8:00 pm ($1.10)
'''
rate = 0
def calc_toll(hour, is_morning, is_weekend):
    # If is_weekend
    if is_weekend == True:
        # If is_morning
        if is_morning == True:
            # If hour < 7 rate = 1.05
            if hour < 7:
                rate = 1.0
            # Else rate = 2.15
            else:
                rate = 2.15
        # Else (not morning)
        else:
            if hour < 8:
                rate = 2.15
            else:
                rate = 1.10
            
            # If hour < 8 rate = 2.15
            # Else rate = 1.10
    else:
        if is_morning == True:
            if hour < 7:
                rate = 1.15
            elif hour < 10:
                rate = 2.95
            else:
                rate = 1.90
        else:
            if hour < 3:
                rate = 1.90
            elif hour < 8:
                rate = 3.95
            else:
                rate = 1.40
    return rate
    
if __name__ == '__main__':
    print(calc_toll(8, True, False))
    print(calc_toll(1, False, False))
    print(calc_toll(3, False, True))
    print(calc_toll(5, True, True))