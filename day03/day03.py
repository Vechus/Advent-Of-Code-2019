with open('in03.txt', 'r') as f:
	wire1 = f.readline().split(',')
	wire2 = f.readline().split(',')

def man(point):
	return sum(map(abs, point))

def path(elem):
	x, y = 0, 0
	wire = {}
	i = 0
	for e in elem:
		d = e[0]
		count = int(e[1:])

		for _ in range(count):
			i += 1
			if d == 'R':
				x += 1
			elif d == 'U':
				y += 1
			elif d == 'L':
				x -= 1
			elif d == 'D':
				y -= 1

			wire[x,y] = i
	return wire

wire1_path = path(wire1)
wire2_path = path(wire2)

inters = set(wire1_path) & set(wire2_path)

distances = { man(point): wire1_path[point] + wire2_path[point] for point in inters }

print(min([man(i) for i in inters]))
print(min(distances.values()))