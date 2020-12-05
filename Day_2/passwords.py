import numpy as np
import pandas as pd
df=pd.read_csv('input.csv', sep=',',header=None)
df.values

data = df[0]

result = 0


for line in data:
	first, second = line.split('-')
	lower = first
	second, third = second.split(':')
	upper, target = second.split()
	matches=0
	
	cond1 = False
	cond2 = False
	for i in range(len(third)):
		if(i==int(lower) and third[i]==target):
			cond1 = True
		if(i==int(upper) and third[i]==target):
			cond2 = True

	if(cond1 == True and cond2 == False):
		result+=1
	if(cond1 == False and cond2 == True):
		result+=1