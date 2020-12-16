import math

file_input = 'input.txt'
ranges = []
myticket = []
nearby_tickets = []

with open(file_input, encoding='utf-8') as file:
    contents = file.read()
    inputs    = contents.split('\n')

zone = 1
for i in range(len(inputs)):
	if(inputs[i]==''):
		zone+=1
		continue
	if(zone == 1):
		right_half = inputs[i].split(': ')[1]
		bounds = right_half.split(' or ')
		left_bounds = bounds[0]
		right_bounds = bounds[1]
		left_lower = left_bounds.split('-')[0]
		left_upper = left_bounds.split('-')[1]
		right_lower = right_bounds.split('-')[0]
		right_upper = right_bounds.split('-')[1]

		cur_list = [left_lower, left_upper, right_lower, right_upper]
		ranges += [cur_list]

	if(zone==2):
		if(inputs[i]=='your ticket:'):
			continue
		else:
			myticket = inputs[i].split(',')

	if(zone==3):
		if(inputs[i]=='nearby tickets:'):
			continue
		else:
			nearby_tickets += [inputs[i].split(',')]



invalid_fields=[]

for x in nearby_tickets:
	for y in x:
		invalid = [False for x in range(len(ranges))]
		for i in range(len(ranges)):
			if not ((int(ranges[i][0])<= int(y) and int(ranges[i][1])>=int(y)) or (int(ranges[i][2])<=int(y) and int(ranges[i][3])>=int(y))):
				invalid[i] = True
				
		if all (invalid):
			invalid_fields += [int(y)]

print(len(invalid_fields))
print(sum(invalid_fields))