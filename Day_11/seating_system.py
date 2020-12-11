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

table = [['L' for c in range(column+2)] for r in range(rows+2)]

for i in range(1, rows+1):
	for j in range(1, column+1):
		table[i][j] = data[i-1][j-1]


def update_table():
	oldtable = copy.deepcopy(table)
	change = False
	for i in range(1, rows+1):
		for j in range(1, column+1):
			## Check if an empty seat should be change to an occupied seat
			update_free_seat = True
			for k in range(-1, 2):
				for r in range(-1, 2):
					if(oldtable[i][j]=='L' and oldtable[i+k][j+r]=='#'):
						update_free_seat = False
			if(update_free_seat and oldtable[i][j]=='L'):
				table[i][j] = '#'

			##Check if an occupied seat should become an empty seat
			occupied_seats = 0
			for k in range(-1, 2):
				for r in range(-1, 2):
					if(k==0 and r==0):
						continue
					if(oldtable[i][j]=='#' and oldtable[i+k][j+r]=='#'):
						occupied_seats += 1

			if(occupied_seats>=4):
				table[i][j] = 'L'

			if(oldtable[i][j]!=table[i][j]):
				change = True
	return change


def check_if_changes_occured():
	change = True
	count = 0
	while(change):
		pretty_print(table)
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