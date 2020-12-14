import math
lines_of_code = []

file_input = 'input.txt'
with open(file_input, encoding='utf-8') as file:
    contents = file.read()
    inputs    = contents.split('\n')

for index, i in enumerate(inputs):
    data     = i.split(' = ')
    lines_of_code.append(data)


def check_bit(n, index): 
    if n & (1 << (index - 1)): 
        return True 
    else: 
        return False

def calculate_int_with_mask(number, mask):
	##Do something clever
	for i in reversed(range(len(mask))):
		if(mask[i]=='X'):
			continue
		elif(mask[i]=='1'):
			if(check_bit(number, len(mask)-i)):
				continue
			else:
				number+= pow(2, len(mask)-i-1)
		elif(mask[i]=='0'):
			if(check_bit(number, len(mask)-i)):
				number -= pow(2, len(mask)-i-1)
			else:
				continue
	return number


def emulate_docking(lines_of_code):
	##Do something clever
	memory = {}
	cur_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	for i in range(len(lines_of_code)):
		if(lines_of_code[i][0] == 'mask'):
			cur_mask = lines_of_code[i][1]
		if(lines_of_code[i][0][:3]=='mem'):
			cur_mem = lines_of_code[i][0][4:]
			cur_mem = int(cur_mem[:-1])
			cur_value = int(lines_of_code[i][1])
			memory[cur_mem] = calculate_int_with_mask(cur_value, cur_mask)

	result=0
	for key in memory:
		result += memory[key]

	return result
				

print(emulate_docking(lines_of_code))