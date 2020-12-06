import os
#from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]


def seat_id(line):
	lb = 0
	ub = 128
	row = 0

	for y in range(0, 7):
		ch = line[y]
		mid = lb + (ub - lb) // 2
		if ch == 'F':
			ub = mid
		else:
			lb = mid
	row = lb
	lb = 0
	ub = 8
	for x in range(0, 3):
		ch = line[x + 7]
		mid = lb + (ub - lb) // 2
		if ch == 'L':
			ub = mid
		else:
			lb = mid
	col = lb
	return row*8 + col

assert(seat_id('BFFFBBFRRR') == 567)
max_id = 0
min_id = 65536
seats = [0]*65536
for line in lines:
	id = seat_id(line)
	max_id = max(max_id, id)
	min_id = min(min_id, id)
	seats[id] = id

for seat in range(min_id,max_id):
	# print(seats[seat])
	if (seats[seat] == 0):
		print(seat)
		break
print(max_id)
