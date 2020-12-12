import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
#lines = [line.strip() for line in open(sdir + "/test.txt").readlines()]

pos = [0,0]
dir=[1,0]
D = {
	'N':[0,1],
	'E':[1,0],
	'S':[0,-1],
	'W':[-1,0]
	}
for line in lines:
	c = line[0]
	v = int(line[1:])
	a = None
	if c in D:
		dd = D[c]
	elif c == 'L':
		dd = [0,0]
		a = [-1,1]
	elif c == 'R':
		dd = [0,0]
		a = [1,-1]
	elif c == 'F':
		dd = dir
		
	if (a):
		assert(0 == v % 90)
		for i in range(0, v, 90):
			dir = [a[0]*dir[1],a[1]*dir[0]]
	else:
		pos = [pos[0] + dd[0] * v, pos[1] + dd[1] * v]

def manhattan(p):
	return abs(p[0]) + abs(p[1])
p1 = manhattan(pos)
p2 = 0

print(p1)
print(p2)