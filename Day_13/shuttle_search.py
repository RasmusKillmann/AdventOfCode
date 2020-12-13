import math

file_input = 'input.txt'
bus_ids = []

with open(file_input, encoding='utf-8') as file:
    contents = file.read()
    inputs    = contents.split('\n')

for index, i in enumerate(inputs):
    data     = i.split(',')
    bus_ids.append(data)


target = int(bus_ids[0][0])
bus_routes = bus_ids[1]


new_bus_routes = []
offsets = []
for i in range(len(bus_routes)):
	if(bus_routes[i]!='x'):
		new_bus_routes.append(int(bus_routes[i]))
		offsets.append(i)

def lcm_func(a, b):
    return abs(a*b) // math.gcd(a, b)

lcm = int(new_bus_routes[0])
timestamp = 0

for i in range(1, len(new_bus_routes)):
	offsets[i] = -offsets[i] % new_bus_routes[i]
	k = (offsets[i] - timestamp) * pow(lcm, -1, new_bus_routes[i]) % new_bus_routes[i]
	lcm_new = lcm_func(lcm, new_bus_routes[i])
	timestamp = (lcm*k + timestamp) % lcm_new
	lcm = lcm_new

print(timestamp)