
input_file = "day_1_input.txt"
counter = 0
window_size = 3 # set this to 1 for the first part
last_values = [None for _ in range(window_size)]
with open(input_file) as f:
	for i, line in enumerate(f.readlines()):
		measurement = int(line.strip())

		if i < window_size:
			last_values[i] = measurement
			continue

		total = measurement + sum(last_values[1:])

		if total > sum(last_values):
			counter += 1
		last_values = last_values[1:] + [measurement]
print(counter)



