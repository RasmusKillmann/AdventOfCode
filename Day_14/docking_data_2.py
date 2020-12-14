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

def calculate_adress(adress):
	cur = 0
	for i in reversed(range(len(adress))):
		if(adress[i] == '1'):
			cur += pow(2, len(adress)-i-1)
	return cur

def update_adresses(memory, mem_adress, value, mask):
	new_adress = ''
	counter = 0
	for i in range(len(mask)):
		if(mask[i]=='X'):
			new_adress+='X'
			counter+=1
		if(mask[i]=='0'):
			if(check_bit(mem_adress, len(mask)-i)):
				new_adress+='1'
			else:
				new_adress+='0'
		if(mask[i]=='1'):
			new_adress+='1'

	adresses = output_adresses_iterative(new_adress, counter)

	for i in range(len(adresses)):
		memory_adress = calculate_adress(adresses[i])
		memory[memory_adress] = value

	return memory
	
def generate_binary(n):

  bin_arr = []
  bin_str = [0] * n

  for i in range(0, int(math.pow(2,n))):

    bin_arr.append("".join(map(str,bin_str))[::-1])
    bin_str[0] += 1

    # Iterate through entire array if there carrying
    for j in range(0, len(bin_str) - 1):

      if bin_str[j] == 2:
        bin_str[j] = 0
        bin_str[j+1] += 1
        continue

      else:
        break

    
  return bin_arr

def output_adresses_iterative(new_adress, number_of_x):
	binary_numbers = generate_binary(number_of_x)
	resulting_list = []
	for i in range(len(binary_numbers)):
		counter=0
		cur_string = ''
		for j in range(len(new_adress)):
			if(new_adress[j]!='X'):
				cur_string += new_adress[j]
				continue
			else:
				cur_string += binary_numbers[i][counter]
				counter+= 1
		resulting_list = resulting_list + [cur_string]
	return resulting_list



def emulate_docking(lines_of_code):
	memory = {}
	cur_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	for i in range(len(lines_of_code)):
		if(lines_of_code[i][0] == 'mask'):
			cur_mask = lines_of_code[i][1]
		if(lines_of_code[i][0][:3]=='mem'):
			cur_mem = lines_of_code[i][0][4:]
			cur_mem = int(cur_mem[:-1])
			cur_value = int(lines_of_code[i][1])
			memory = update_adresses(memory, cur_mem, cur_value, cur_mask)
	
	result = 0
	
	for key in memory:
		result += memory[key]

	return result

print(emulate_docking(lines_of_code))

