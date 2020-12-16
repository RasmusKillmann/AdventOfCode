import numpy as np
import pandas as pd
import sys
df=pd.read_csv('input.csv', sep=',',header=None)


n = len(df)

words = {}

for i in range(7):
	key = int(df[i])
	words[key] = i

cur_num = 0
for i in range(7, 30000000-1):
	if cur_num not in words.keys():
		words[cur_num] = i
		cur_num = 0
	else:
		last_time = words[cur_num] 
		words[cur_num] = i
		cur_num = i - last_time
print(cur_num)