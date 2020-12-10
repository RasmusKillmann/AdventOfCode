import numpy as np
import pandas as pd
import sys
df=pd.read_csv('input.csv', sep=',',header=None)
data = df[0]

n = len(data)
array = [0 for i in range (n)]

for i in range(n):
	array[i] = int(data[i])

array.sort()

def find_jolts():
	jolts = [0,0,0]

	for i in range(n):
		if(i==0):
			jolts[array[i]-1] += 1
			continue
		cur_jolt = array[i]-array[i-1]
		jolts[cur_jolt-1] += 1

	jolts[2] += 1

	return jolts


print(find_jolts()[0]*find_jolts()[2])

def find_arrangements():
	jolts = [0 for i in range(n+1)]
	for i in range(n):
		if(i==0):
			jolts[i] = array[i]
			continue
		jolts[i] = array[i] - array[i-1]
	jolts[n] = 3

	numberOfArrangements = [0 for i in range(n+1)]

	numberOfArrangements[n] = 1

	for i in reversed(range(n)):
		if(jolts[i] == 1):
			numberOfArrangements[i] += numberOfArrangements[i+1] 

		if(jolts[i] == 3):
			numberOfArrangements[i] += numberOfArrangements[i+1] 

		if(jolts[i]==1 and jolts[i+1]==1):
			numberOfArrangements[i] += numberOfArrangements[i+2]

		if(jolts[i]==1 and jolts[i+1]==1 and jolts[i+2]==1):
			numberOfArrangements[i] += numberOfArrangements[i+3]
		
	return numberOfArrangements[0]

print(find_arrangements())