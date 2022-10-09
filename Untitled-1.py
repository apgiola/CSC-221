is_leap_year = False
   
input_year = int(input())
year = 0
year2 = 1
year3 = 0
hundreds = 0

while is_leap_year == False:
    if input_year % 4 == 0:
        year = 1
    if input_year % 100 == 0:
        hundreds = 1
        year2 = input_year % 400
    if (year == 1) and (year2 == 0) or (year == 1) and (hundreds == 0):
        print(input_year, "- leap year")
        is_leap_year = True
        
    else:
        print(input_year, "- not a leap year")
        year = 0
        year2 = 1
        break
        