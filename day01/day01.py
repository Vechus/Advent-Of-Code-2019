import math

f = open('in01.txt', 'r')
instr = f.read()

x = 0

#p1
for i in instr.split('\n'):
	x += math.floor(int(i) / 3) - 2

print('P1: ' + x)

#p2
y = 0

for i in instr.split('\n'):
	y = math.floor(int(i)/3 - 2)
	x += y
	while(1):
		y = math.floor(int(y) / 3 - 2)
		if y <= 0:
			break
		else:
			x += y

print('P2: ' + x)