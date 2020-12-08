import numpy as np
import pandas as pd
df=pd.read_csv('input.csv', sep=',',header=None)
data = df[0]

n = len(data)

def check_for_loops1(query_data):
	i=0
	acc = 0
	query_tickmarks = [0 for i in range(n+1)]
	while query_tickmarks[i]!=1:
		if(i==n):
			return (query_tickmarks, True, acc)
		curopp = query_data[i].split(' ')[0]
		curvalue = query_data[i].split(' ')[1]
		query_tickmarks[i] = 1
		if(curopp == 'nop'):
			i+=1
			continue
		if(curopp == 'acc'):
			if(curvalue[0]=='+'):
				acc += int(curvalue[1:])
			else:
				acc -= int(curvalue[1:])
			i+=1
			continue
		if(curopp == 'jmp'):
			if(curvalue[0]=='+'):
				i += int(curvalue[1:])
			else:
				i-= int(curvalue[1:])
			continue
	return (query_tickmarks, False, acc)

tickmarks = check_for_loops1(data)[0]


def check_which_instruction_to_change():
	newdata = None
	query_data = data.copy()
	for i in range(len(tickmarks)):
		if(tickmarks[i]==0):
			continue
		if(data[i][:3] =='acc'):
			continue
		if(data[i][:3]=='jmp'):
			newdata = 'nop' + data[i][3:]
		if(data[i][:3]=='nop'):
			newdata = 'jmp' + data[i][3:]
		query_data = data.copy()
		query_data[i] = newdata
		if(check_for_loops1(query_data)[1]):
			print(check_for_loops1(query_data)[2])

check_which_instruction_to_change()