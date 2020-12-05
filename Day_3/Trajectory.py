import numpy as np
import pandas as pd
df=pd.read_csv('input.csv', sep=',',header=None)
data = df[0]

### Solution 1

print(data)
result=0
for i in range(1,len(data)):
	column = (3*i) % len(data[i]) 
	if(data[i][column]=='#'):
		result+=1

print(result)



### Solution 2


result1 = 0
result2 = 0
result3 = 0
result4 = 0
result5 = 0

for i in range(1,len(data)):
	column1 = i % len(data[i]) 
	column2 = (3*i) % len(data[i])
	column3 = (5*i) % len(data[i])
	column4 = (7*i)%len(data[i])
	
	if(data[i][column1]=='#'):
		result1+=1

	if(data[i][column2]=='#'):
		result2+=1

	if(data[i][column3]=='#'):
		result3+= 1

	if(data[i][column4]=='#'):
		result4+=1

	
i=2
j=1
while i<len(data):
	column5 = j%len(data[i])
	if(data[i][column5]=='#'):
		result5+=1
	i+=2
	j+=1

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

print(result1*result2*result3*result4*result5)