import copy
file_input = 'input.txt'

with open(file_input, encoding='utf-8') as file:
    contents = file.read()
    inputs    = contents.split('\n')

colums = len(inputs[0])
rows = len(inputs)

cube_map = [[[[0 for q in range(20)] for k in range(20)] for j in range(20)] for i in range(20)]

for i in range(6, 14):
	for j in range(6, 14):
		if(inputs[i-6][j-6]=='#'):
			cube_map[i][j][10][10] = 1

def checkneighbours(x, y, z, q, mapping):
	result = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			for k in range(-1, 2):
				for w in range(-1, 2):
					if(i==0 and j==0 and k==0 and w==0):
						continue
					if(int(mapping[x + i][y + j][z + k][q + w])==1):
						result += 1
	return result


def one_iteration():
	previous_mapping = copy.deepcopy(cube_map)
	for i in range(19):
		for j in range(19):
			for k in range(19):
				for w in range(19):
					number_of_neighbors = checkneighbours(i, j, k, w, previous_mapping)
					if(int(previous_mapping[i][j][k][w]) == 1 and (number_of_neighbors==2 or number_of_neighbors==3)):
						cube_map[i][j][k][w]=1
					elif(int(previous_mapping[i][j][k][w])==1):
						cube_map[i][j][k][w]=0
					elif(int(previous_mapping[i][j][k][w])==0 and number_of_neighbors==3):
						cube_map[i][j][k][w]=1
					elif(int(previous_mapping[i][j][k][w])==0):
						cube_map[i][j][k][w]=0

for i in range(6):
	one_iteration()

result = 0

for i in range(20):
	for j in range(20):
		for k in range(20):
			for w in range(20):
				result += cube_map[i][j][k][w]

print(result)
