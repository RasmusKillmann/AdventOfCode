import numpy as np
file_input = 'input.txt'
bags  = []
bagstonumbers={}


with open(file_input, encoding='utf-8') as file:
    contents = file.read()
    inputs    = contents.split('\n')

for index, i in enumerate(inputs):
    data     = i.replace('.', '').split('\n')
    bags.append(data)

table = np.zeros((len(bags), len(bags)))

for i in range(0, len(bags)):
	newbag = (bags[i][0].split(" contain"))[0]
	bagstonumbers.update({newbag:i})




for i in range(0, len(bags)-1):
	frombag = bags[i][0].split(" contain ")[0]

	frombagnumber = bagstonumbers.get(frombag)

	targetbags = bags[i][0].split(" contain ")[1]

	splitbags = targetbags.split(", ")

	if(splitbags[0]=='no other bags'):
		continue

	for j in range(0, len(splitbags)):
		numberofbags = int(splitbags[j][0])
		print(numberofbags)
		tobag = splitbags[j][2:]

		if(tobag[-1] != 's'): 
			tobag  = tobag + 's'

		tobagnumber = bagstonumbers.get(tobag)

		table[frombagnumber, tobagnumber] = int(numberofbags)



def countchildren(targetindex):
	result = 1
	for i in range(0, len(bags)):
		if(table[targetindex][i] >= 1):
			result += countchildren(i)*table[targetindex][i]
	return result

print(countchildren(bagstonumbers.get('shiny gold bags'))-1)