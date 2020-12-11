import numpy as np
import pandas as pd
import sys
df=pd.read_csv('input.csv', sep=',',header=None)
data = df[0]

rows = len(data)
column = len(data[0])
import copy

def pretty_print(table):
	for i in range(len(table)):
		concatstring=''
		for j in range(len(table[i])):
			concatstring += table[i][j]
		print(concatstring)
	print('--------------------------------.--------------------------------')

table = [['W' for c in range(column+2)] for r in range(rows+2)]



for i in range(1, rows+1):
	for j in range(1, column+1):
		table[i][j] = data[i-1][j-1]


def update_table():
	oldtable = copy.deepcopy(table)
	change = False
	for i in range(1, rows+1):
		for j in range(1, column+1):
			## Check if an empty seat should be change to an occupied seat
			occupied_seats = count_visible_occupied_seats(i, j, oldtable)
			if(oldtable[i][j]=='L' and occupied_seats==0):
				table[i][j] = '#'

			if(oldtable[i][j]=='#' and occupied_seats>=5):
				table[i][j]= 'L'

			if(oldtable[i][j]!=table[i][j]):
				change = True
	return change

def count_visible_occupied_seats(row_index, column_index, table):
	count = 0

	for i in range(1, len(table)):
		currentchar = table[i+row_index][column_index]
		if(currentchar=='#'):
			count+=1
			break
		if(currentchar=='L' or currentchar=='W'):
			break

	for i in range(1, len(table)):
		currentchar = table[row_index-i][column_index]
		if(currentchar=='#'):
			count+=1
			break
		if(currentchar=='L' or currentchar == 'W'):
			break

	for j in range(1, len(table)):
		currentchar = table[row_index][j+column_index]
		if(currentchar=='#'):
			count+=1
			break
		if(currentchar=='L' or currentchar=='W'):
			break

	for j in range(1, column_index):
		currentchar = table[row_index][column_index-j]
		if(currentchar=='#'):
			count+=1
			break
		if(currentchar=='L' or currentchar=='W'):
			break

	for i in range(1, len(table)):
		currentchar =table[i+row_index][i+column_index] 
		if(currentchar=='#'):
			count+=1
			break
		if(currentchar=='L' or currentchar=='W'):
			break

	for i in range(1, len(table)):
		currentchar = table[row_index+i][column_index-i]
		if(currentchar=='#'):
			count+=1
			break
		if(currentchar=='L' or currentchar=='W'):
			break

	for j in range(1, len(table)):
		currentchar = table[row_index-j][column_index+j]
		if(currentchar=='#'):
			count+=1
			break
		if(currentchar=='L' or currentchar=='W'):
			break

	for j in range(1, len(table)):
		currentchar = table[row_index-j][column_index-j]
		if(currentchar=='#'):
			count+=1
			break
		if(currentchar=='L' or currentchar=='W'):
			break

	return count


def check_if_changes_occured():
	change = True
	count = 0
	while(change):
		change = update_table()


def count_occupied_seats():
	check_if_changes_occured()
	count=0
	for i in range(rows+1):
		for j in range(column+1):
			if(table[i][j]=='#'):
				count+= 1
	return count


print(count_occupied_seats())