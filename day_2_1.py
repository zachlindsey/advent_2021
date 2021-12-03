input_file = 'day_2_input.txt'

depth = 0
hpos = 0

with open(input_file) as f:
	for line in f.readlines():
		cmd, value = line.split(' ')
		value = int(value.strip())
		if cmd == 'forward':
			hpos += value
		elif cmd == 'up':
			depth -= value
		elif cmd == 'down':
			depth += value
		else:
			raise(f"invalid command {cmd}")

print(depth*hpos)