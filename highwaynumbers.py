#Take user input and check if valid
highway_num = int(input())
if highway_num < 1 or highway_num > 999:
    print('{} is not a valid highway number'.format (highway_num))
    quit()
#type of highway and what primary it services
if highway_num > 100:
    road_type = 'auxiliary'
    serving = str(highway_num % 100)
else:
    road_type = 'primary'
    serving = ''

#direction of service
if highway_num % 2 == 0:
    going = 'east/west'
else:
    going = 'north/south'

#output create list
output = ['I-{}'.format(highway_num), 'is', road_type + ',']
if serving:
    output.extend(['serving', 'I-{},'.format(serving)])
output.extend(['going', going])
print(' '.join(output))