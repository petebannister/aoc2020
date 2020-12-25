import os
import copy
import math

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]


def solve(lines):
	r1 = 0
	r2 = 0
	tiles = {}
	# skewed grid
	ins = {
		'e':(1,0),
		'w':(-1,0),
		'ne':(0,1),
		'se':(1,-1),
		'nw':(-1,1),
		'sw':(0,-1)
	}
	black = False
	white = True

	def get_coord(line, pos, n):
		if (pos + n) <= len(line):
			s = line[pos:pos+n]
			if s in ins:
				return ins[s]
		return None

	for line in lines:
		i = 0
		x, y = (0,0)
		while i < len(line):
			coord = get_coord(line, i, 2)
			if (coord == None):
				coord = get_coord(line,i,1)
				i = i + 1
			else:
				i = i + 2

			x, y = (coord[0] + x, coord[1] + y)
			coord = (x,y)
		if (coord in tiles):
			tiles[coord] = not tiles[coord]
		else:
			tiles[coord] = black

	# count black tiles (0s)
	for v in tiles.values():
		if v == black:
			r1 += 1

	# Conway the sh*t out of it
	dirs = ins.values()
	for i in range(0, 100):
		print(i)
		# expand - could improve speed by only adding those we need to
		newtiles = set()
		flip = set()
		for coord in tiles.keys():
			for d in dirs:
				chk = (coord[0] + d[0], coord[1] + d[1])
				if chk not in tiles:
					newtiles.add(chk)
		for coord in newtiles:
			tiles[coord] = white
		# simulate
		for coord in tiles.keys():
			nblack = 0
			for d in dirs:
				chk = (coord[0] + d[0], coord[1] + d[1])
				if chk in tiles:
					if tiles[chk] == black:
						nblack = nblack + 1
			if tiles[coord] == black:
				if nblack == 0 or nblack > 2:
					flip.add(coord)
			else:
				if nblack == 2:
					flip.add(coord)
		# update
		for coord in flip:
			tiles[coord] = not tiles[coord]
	
	# count black tiles (0s)
	for v in tiles.values():
		if v == black:
			r2 += 1

	return (r1, r2)

t1, t2 = solve(test)
print('t1:', t1)
print('t1:', t2)
assert(t1 == 10)
assert(t2 == 2208)

p1, p2 = solve(lines)
print('p1:', p1)
assert(p1 == 232)
print('p2:', p2)
