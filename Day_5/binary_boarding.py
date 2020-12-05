import numpy as np
import pandas as pd
df=pd.read_csv('input.csv', sep=',',header=None)
data = df[0]


result = 0
seats = [ [ 0 for i in range(8) ] for j in range(128) ]

for i in range(0, len(data)):
	curRow = data[i]
	top = 127
	bot = 0
	mid = 63
	for j in range(0, 7):
		if(curRow[j]=="B"):
			bot = mid + 1
			mid = int((top + mid)/2)
		else:
			top = mid
			mid = int((bot + mid)/2)
	
	row = bot

	top = 7
	bot = 0
	mid = 3

	for j in range(0, 3):
		if(curRow[j+7]=="R"):
			bot = mid +1
			mid = int((top + mid)/2)
		else:
			top = mid
			mid = int((bot + mid)/2)


	column = bot

	seats[row][column] = 1

	if(result<= row*8 + column):
		result = row*8 + column

for i in range(0, 128):
	if (seats[i][0]==0 and seats[i][1]==0):
		continue
	for j in range(0, 6):
		if(seats[i][j]==1 and seats[i][j+1]==0 and seats[i][j+2]==1):
			print(i*8 + j+1)