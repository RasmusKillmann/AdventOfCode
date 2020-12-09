import numpy as np
import pandas as pd
import sys
df=pd.read_csv('input.csv', sep=',',header=None)
data = df[0]

n = len(data)

def find_non_summable_number(preamble_size):

	preamble = [0 for i in range(preamble_size)]
	for i in range(n):
		cur = False
		if(i<preamble_size):
			preamble[i] = int(data[i])
			continue
		for j in range(len(preamble)):
			for k in range(len(preamble)):
				if(preamble[j] + preamble[k] ==int(data[i])):
					preamble[i % preamble_size] = int(data[i])
					cur = True
		if(cur==False):
			return int(data[i])

print(find_non_summable_number(25))		


def find_contiguous_set(input):
	summarable = 0
	for i in range(n):
		summarable = 0
		for j in range(i, n):
			summarable = sum(data[i:j])
			if(i==j):
				continue
			if(summarable>input):
				continue
			if(summarable == input):
				return max(data[i:j]) + min(data[i:j])



print(find_contiguous_set(find_non_summable_number(25)))