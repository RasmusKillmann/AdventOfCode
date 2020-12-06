# -- Vars. --
file_input = 'input.txt'
groups  = []
counter    = 0

# -- Open File --
with open(file_input, encoding='utf-8') as file:
    contents = file.read()
    inputs    = contents.split('\n\n')

for index, i in enumerate(inputs):
    data     = i.replace('\n',' ').split()
    groups.append(data)

result = 0
for i in range(0, len(groups)):
	cur = set(groups[i][0])
	for j in range(0, len(groups[i])):
		nextone = set(groups[i][j])
		current = cur.intersection(nextone)
		cur = current
	result+= len(cur)
print(result)