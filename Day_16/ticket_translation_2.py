import math
from collections import defaultdict

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



valid_tickets=[]

for x in nearby_tickets:
	a_invalid_entry = False
	for y in x:
		invalid = [False for x in range(len(ranges))]
		for i in range(len(ranges)):
			if not ((int(ranges[i][0])<= int(y) and int(ranges[i][1])>=int(y)) or (int(ranges[i][2])<=int(y) and int(ranges[i][3])>=int(y))):
				invalid[i] = True
		if all (invalid):
			a_invalid_entry = True

	if not (a_invalid_entry):
		valid_tickets += [x]

n = len(ranges)

table = [[[0 for k in range(n)] for j in range(n)] for i in range(len(valid_tickets))]

def check_lower_upper_bounds(value, bounds):
	return (int(value)>= int(bounds[0]) and int(value) <= int(bounds[1])) or (int(value)>= int(bounds[2]) and int(value)<=int(bounds[3]))

for index, x  in enumerate(valid_tickets):
	for i in range(len(x)):
		for j in range(len(ranges)):
			if (check_lower_upper_bounds(x[i], ranges[j])):
				table[index][i][j] = 1


range_to_column = [[1 for k in range(n)] for j in range(n)]

for i in range(len(valid_tickets)):
	for j in range(n):
		for k in range(n):
			if not(table[i][j][k]):
				range_to_column[k][j] = 0

final_range_to_column = {}



while(len(final_range_to_column)<n):
	for i, x in enumerate(range_to_column):
		if(x.count(1)==1):
			for j, y in enumerate(x):
				if(y==1):
					final_range_to_column[i] = j
					cur_column = j
			for i, x in enumerate(range_to_column):
				range_to_column[i][cur_column] = 0



result = 1

for i in range(6):
	result*= int(myticket[final_range_to_column[i]])

print(result)