#Take user input and check if valid
highway_num = int(input())
if highway_num < 1 or highway_num > 999 or highway_num % 100 == 0:
    print('{} is not a valid interstate highway number.'.format (highway_num))
    quit()
#type of highway and what primary it services
if highway_num > 100:
    road_type = 'auxiliary'
    auxiliary = highway_num % 100
else:
    road_type = 'primary'
    auxiliary = ''

#direction of service
if highway_num % 2 == 0:
    direction = 'east/west.'
else:
    direction = 'north/south.'

#output create list
output = ['I-{}'.format(highway_num), 'is', road_type + ',']
#create output branch to add to output variable if it is an auxiliary highway.
if auxiliary:
    output.extend(['serving', 'I-{},'.format(auxiliary)])
#adds the direction of the highway to the output variable
output.extend(['going', direction])
print(' '.join(output))