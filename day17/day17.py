import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

p1 = 0
p2 = 0
seq3 = []
seq4 = []
for z in range(-1,2):
	for y in range(-1,2):
		for x in range(-1,2):
			if x or y or z:
				seq3.append((x,y,z))


for z in range(-1,2):
	for y in range(-1,2):
		for x in range(-1,2):
			for w in range(-1,2):
				if x or y or z or w:
					seq4.append((x,y,z,w))

def grid3(input):
	grid = set()
	for y,line in enumerate(input):
		for x,c in enumerate(line):
			if (c == '#'):
				grid.add((x,y,0))
	return grid

def grid4(input):
	grid = set()
	for y,line in enumerate(input):
		for x,c in enumerate(line):
			if (c == '#'):
				grid.add((x,y,0,0))
	return grid
def add_coord(a, b):
	#return tuple(map(lambda i, j: i + j, a, b))
	return tuple(map(sum, zip(a, b))) 

def solve(grid, N, seq):
	additions = set()
	removals = set()
	inactive = set()
	for i in range(0, N):
		print("step:", i)
		additions.clear()
		removals.clear()
		inactive.clear()
		for coord in grid:
			neighbors = 0
			for dc in seq:
				c2 = add_coord(coord, dc)
				if c2 in grid:
					neighbors += 1
				else:
					inactive.add(c2)
			# active cell:
			# If a cube is active and exactly 2 or 3 
			# of its neighbors are also active, the cube
			# remains active. Otherwise, the cube becomes inactive.
			if (not(2 <= neighbors <= 3)):
				removals.add(coord)
				
		for coord in inactive:
			neighbors = 0
			for dc in seq:
				c2 = add_coord(coord, dc)
				if c2 in grid:
					neighbors += 1
			# If a cube is inactive but exactly 3 of 
			# its neighbors are active, the cube becomes 
			# active. Otherwise, the cube remains inactive.
			if (neighbors == 3):
				additions.add(coord)

		# update grid
		grid.update(additions)
		grid.difference_update(removals)
		
	return len(grid)

t1 = solve(grid3(test), 6, seq3)
print(t1)
assert(t1 == 112)

t2 = solve(grid4(test), 6, seq4)
print(t2)
assert(t2 == 848)

p1 = solve(grid3(lines), 6, seq3)
print('p1:', p1)
p2 = solve(grid4(lines), 6, seq4)
print('p2:', p2)
