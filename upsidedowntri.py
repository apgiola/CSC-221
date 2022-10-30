#usr input
num_input = int(input())
#create blank list
lst = []
#create list with all ints between 0 and final usr input
for i in range(1, num_input + 1):
    lst.append(i)
lst.reverse() #reverse list
for j in lst: #print stars with the reversed list.
    print('* ' * j)