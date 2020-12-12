import numpy as np
import pandas as pd
import sys
df=pd.read_csv('input.csv', sep=',',header=None)
data = df[0]

n = len(data)

def exercise_1():
	direction =0
	x_cor = 0
	y_cor = 0
	for i in range(n):
		instruction = data[i][0]
		distance = int(data[i][1:])
		if(instruction == 'N'):
			y_cor += distance
		if(instruction == 'S'):
			y_cor -= distance
		if(instruction == 'E'):
			x_cor += distance
		if(instruction == 'W'):
			x_cor -= distance
		if(instruction == 'R'):
			direction = (direction + (distance/90))% 4
		if (instruction == 'L'):
			direction = (direction - (distance/90)) % 4
		if(instruction == 'F'):
			if(direction==0):
				x_cor += distance
			if(direction==1):
				y_cor -= distance
			if(direction==2):
				x_cor -= distance
			if(direction==3):
				y_cor += distance
	
	print(abs(x_cor) + abs(y_cor))

def rotate_90(x, y):
	x_new = y
	y_new = -x
	return x_new, y_new

def exercise_2():
	x_cor = 0
	y_cor = 0
	x_way = 10
	y_way = 1

	for i in range(n):
		instruction = data[i][0]
		distance = int(data[i][1:])
		if(instruction == 'N'):
			y_way += distance
		if(instruction == 'S'):
			y_way -= distance
		if(instruction == 'E'):
			x_way += distance
		if(instruction == 'W'):
			x_way -= distance
		if(instruction == 'F'):
			x_cor += x_way*distance
			y_cor += y_way*distance
		if(instruction == 'R'):
			iteration = int(distance/90)
			for i in range(iteration):
				x_way, y_way = rotate_90(x_way, y_way)
		if(instruction == 'L'):
			iteration = int(4-distance/90)
			for i in range(iteration):
				x_way, y_way = rotate_90(x_way, y_way)

	print(abs(x_cor)+abs(y_cor))

exercise_2()
