f = open('in02.txt', 'r')

strs = f.read().split(',')

arr = [int(n) for n in strs]

def part1(arr, noun=12, verb=2):
	i = 0
	lst = arr[:]
	lst[1] = noun
	lst[2] = verb
	while True:
		if lst[i] == 1:
			lst[ lst[i + 3] ] = lst[ lst[i + 1] ] + lst[ lst[i + 2] ]
		elif lst[i] == 2:
			lst[ lst[i + 3] ] = lst[ lst[i + 1] ] * lst[ lst[i + 2] ]
		elif lst[i] == 99:
			break
		else:
			print('YAMEROOOOOOOOO')
		i += 4

	return lst[0]


def part2(arr):
    for noun in range(100):
        for verb in range(100):
            if part1(arr, noun, verb) == 19690720:
                return 100 * noun + verb


print(part1(arr))
print(part2(arr))