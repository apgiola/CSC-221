def usr_info(age, name, gender=None):
    if gender != None:
        print(f'Hello {name}, you are {age} years old and are a {gender}!')
    else:
        print(f'Hello {name}, you are {age} years old!') 
age = int(input())
name = input()
gender = input()
usr_info(age, name, gender)
usr_info(age, name)

foods = ["Cherry", "Strawberry", "Blueberry"]
for i in foods:
    print(i, end=' ')