import copy
file_input = 'input.txt'

with open(file_input, encoding='utf-8') as file:
    contents = file.read()
    inputs    = contents.split('\n')

for i in range(len(inputs)):
	inputs[i] = inputs[i].replace(' ', '')


def calculate_end_parenthesis(expression):
	level = 0
	for i in range(len(expression)):
		if(expression[i]=='('):
			level += 1
		if(expression[i]==')'):
			level -= 1
		if(expression[i]==')' and level==0):
			return i

def evaluate_exp(expression):
	cur_op = '+'
	result = 0
	i = 0
	while i < len(expression):
		if(expression[i]=='('):
			end_position = calculate_end_parenthesis(expression[i:])
			if(cur_op=='+'):
				result+= evaluate_exp(expression[i+1:i+end_position+1])
			if(cur_op=='*'):
				result*= evaluate_exp(expression[i+1:i+end_position+1])
			i+= end_position
			continue
		if(expression[i]==')'):
			i+= 1
			continue
		if(expression[i]=='*'):
			i+=1
			cur_op = '*'
			continue
		if(expression[i]=='+'):
			i+=1
			cur_op = '+'
			continue
		if(cur_op=='+'):
			result += int(expression[i])
			i+=1
			continue
		if(cur_op=='*'):
			result *= int(expression[i])
			i+=1
			continue

	return result



def calculate_result(data):
	result = 0
	for i in range(len(data)):
		cur = evaluate_exp(data[i])
		result += int(cur)
	return result

print(calculate_result(inputs))