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

def calculate_expression(expression):
    answer = []
    cur_ans = 0
    i = 0

    while i < len(expression):
        if(expression[i]=='*'):
            answer.append(cur_ans)
            cur_ans=0

        if(expression[i]=='('):
            end_position = calculate_end_parenthesis(expression[i:])
            cur_ans += calculate_expression(expression[i+1:end_position+i+1])
            i+=end_position

        if(expression[i].isnumeric()):
            cur_ans += int(expression[i])
        i+= 1
    answer.append(cur_ans)

    result = 1
    for i in range(len(answer)):
        result*=answer[i]
    return result

def day_1():
    result = 0
    for i in range(len(inputs)):
        result += calculate_expression(inputs[i])
    print(result)

day_1()