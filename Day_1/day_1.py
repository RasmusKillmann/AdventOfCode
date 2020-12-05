import numpy as np
from numpy import genfromtxt
data = genfromtxt('input.csv', delimiter=',')

for x in data:
	for y in data:
		for z in data:
			result = x+y+z
			if result==2020:
				print(x*y*z)