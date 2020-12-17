import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

p1 = 0
p2 = 0
seq = []
for z in range(-1,2):
	for y in range(-1,2):
		for x in range(-1,2):
			if x or y or z:
				seq.append((x,y,z))

def solve(input, N):
	grid = set()

	for y,line in enumerate(input):
		for x,c in enumerate(line):
			if (c == '#'):
				grid.add((x,y,0))

	for i in range(0, N):
		additions = set()
		removals = set()
		inactive = set()
		for x,y,z in grid:
			neighbors = 0
			for (dx,dy,dz) in seq:
				coord = (x+dx, y+dy, z+dz)
				if coord in grid:
					neighbors += 1
				else:
					inactive.add(coord)
			# active cell:
			# If a cube is active and exactly 2 or 3 
			# of its neighbors are also active, the cube
			# remains active. Otherwise, the cube becomes inactive.
			if (not(2 <= neighbors <= 3)):
				removals.add((x,y,z))
				
		for x,y,z in inactive:
			neighbors = 0
			for (dx,dy,dz) in seq:
				coord = (x+dx, y+dy, z+dz)
				if coord in grid:
					neighbors += 1
			# If a cube is inactive but exactly 3 of 
			# its neighbors are active, the cube becomes 
			# active. Otherwise, the cube remains inactive.
			if (neighbors == 3):
				additions.add((x,y,z))

		# update grid
		grid.update(additions)
		grid.difference_update(removals)
		
	p2 = 0
	p1 = len(grid)
	return (p1, p2)

t1, t2 = solve(test, 6)
print(t1)
print(t2)
assert(t1 == 112)
#assert(t2 == 12)

p1, p2 = solve(lines, 6)

print('p1:', p1)
print('p2:', p2)
