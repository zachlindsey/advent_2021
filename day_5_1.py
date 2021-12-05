
input_file = "day_5_input.txt"

do_part_2 = True

line_counter = {}
with open(input_file) as f:
	for line in f.readlines():
		p1,p2 = line.strip().split(' -> ')
		p1 = list(map(int,p1.split(',')))
		p2 = list(map(int,p2.split(',')))
		
		if p1[0] == p2[0]:
			start = min(p1[1],p2[1])
			stop = max(p1[1],p2[1])
			for y in range(start, stop+1):
				count = line_counter.get((p1[0],y),0)+1
				line_counter[(p1[0],y)] = count

		elif p1[1] == p2[1]:
			start = min(p1[0],p2[0])
			stop = max(p1[0],p2[0])
			for x in range(start,stop+1):
				count = line_counter.get((x,p1[1]),0)+1
				line_counter[(x,p1[1])] = count
		elif do_part_2:
			dx = (p1[0] - p2[0])/abs(p1[0] - p2[0])
			dy = (p1[1] - p2[1])/abs(p1[1] - p2[1])
			for t in range(abs(p1[0]-p2[0])+1):
				x = p2[0] + t*dx
				y = p2[1] + t*dy
				count = line_counter.get((x,y),0)+1
				line_counter[(x,y)] = count

bads = 0
for k in line_counter.keys():
	if line_counter[k] > 1:
		bads += 1
print(bads)
		

