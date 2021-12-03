filename = "day_3_input.txt"

# counters for the number of ones in each bit
one_counter = [0 for _ in range(12)]
oxy_counter = [0 for _ in range(12)]
co2_counter = [0 for _ in range(12)]

# containers for the sets of strings needed for oxygen, co2
oxy_strings = set()
co2_strings = set()
oxy_answer = None
co2_answer = None

total = 0
with open(filename) as f:
	for line in f.readlines():
		total += 1
		oxy_strings.add(line.strip())
		co2_strings.add(line.strip())
		if line[0] == '1':
			oxy_counter[0] += 1
			co2_counter[0] += 1

		for i, c in enumerate(line.strip()):
			if c == '1':
				one_counter[i] += 1
				
					
# do the gamme and epsilon part of the problem
gamma = 0
epsilon = 0
for p, v in enumerate(one_counter[::-1]):
	if v*2 > total:
		gamma += 2**p

	if v*2 <= total:
		epsilon += 2**p

print('gamma:', gamma)
print('epsilon:', epsilon)
print('product:', gamma*epsilon)
print()


# Now, go left to right across the bits of the sets of strings,
# applying the filter critera. 

# Then get the counts of 1s and 0s for the next round.

# Then see if we're down to one string!
for pos in range(12):
	# oxygen
	if oxy_answer is None:
		if 2*oxy_counter[pos] >= len(oxy_strings):
			# 1 is most common or tie
			
			oxy_strings = filter(lambda x: x[pos] == '1', oxy_strings)
			oxy_strings = set(oxy_strings)
		else:
			# 0 is most common
			oxy_strings = filter(lambda x: x[pos] == '0', oxy_strings)
			oxy_strings = set(oxy_strings)

		if pos < 11 and len(oxy_strings) > 1:
			next_counter = 0
			for s in oxy_strings:
				if s[pos+1] == '1':
					next_counter += 1
			oxy_counter[pos+1] = next_counter

		if len(oxy_strings) == 1:
			oxy_answer = list(oxy_strings)[0]

	# co2
	if co2_answer is None:
		if 2*co2_counter[pos] >= len(co2_strings):
			# 1 is most common or tie
			
			co2_strings = filter(lambda x: x[pos] == '0', co2_strings)
			co2_strings = set(co2_strings)
		else:
			# 0 is most common
			co2_strings = filter(lambda x: x[pos] == '1', co2_strings)
			co2_strings = set(co2_strings)

		if pos < 11 and len(co2_strings) > 1:
			next_counter = 0
			for s in co2_strings:
				if s[pos+1] == '1':
					next_counter += 1
			co2_counter[pos+1] = next_counter
		

	

		if len(co2_strings) == 1:
			co2_answer = list(co2_strings)[0]	





co2_answer = int(co2_answer,2)
print('CO2 level:', co2_answer)

oxy_answer = int(oxy_answer,2)
print('oxy level:', oxy_answer)
print('product:', oxy_answer * co2_answer)

