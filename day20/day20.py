import os
import copy
import math

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

def load(lines):
	tiles = {}
	id = 0
	for line in lines:
		if line.endswith(':'):
			id = int(line.split(':')[0].split(' ')[1])
			tiles[id] = []
		elif line:
			tiles[id].append(line)
	return tiles

def edge_value(edge):
	v = 0
	for p in edge:
		v <<= 1
		if p == '#':
			v |= 1
	return v

def reverse_bits(v, bitlen):
	bv = bin(v)
	v = bv[-1:1:-1]
	v = v + (bitlen - len(v))*'0'
	v = int(v,2)
	return v

def rotate_edges(edges, edge_len):
	return (
		reverse_bits(edges[3], edge_len),
		edges[0],
		reverse_bits(edges[1], edge_len),
		edges[2]
	)

def flip_x(edges, edge_len):
	return (
		reverse_bits(edges[0], edge_len), # top
		edges[3],
		reverse_bits(edges[2], edge_len),
		edges[1]
	)

def bin_to_edge(v):
	s = ''
	x = 1 << 9
	while x > 0:
		if 0 == v & x:
			s += '.'
		else:
			s += '#'
		x >>= 1
	return s

def rotated_tile(tile):
	ts = len(tile[0])
	result = ['' for i in range(0,ts)]
	for ty in range(0, ts):
		for tx in range(0, ts):
			ax = tx
			ay = ty
			ax, ay = ay, (ts - 1) - ax
			result[ty] += tile[ay][ax]
	return result

def flip_tile(tile):
	for i,line in enumerate(tile):
		tile[i] = line[::-1]

grid = []
visited = set()

def solve(lines):
	global visited, grid

	tiles = load(lines)
	ntiles = len(tiles)
	print('ntiles: ', ntiles)
	width = int(math.sqrt(ntiles))
	height = width

	edge_len = len(tiles[next(iter(tiles))])
	edge_max = edge_len - 1
	print('edge_len: ', edge_len)

	# Build index
	tile_edges = {}
	edge_map = [{},{},{},{}]
	TOP = 0
	RIGHT = 1
	BOTTOM = 2
	LEFT = 3
	# for each tile calculate a number for each edge (edge_id) so 
	# that edge comparisons are simply an integer comparison. 
	for tile_id, tile in tiles.items():
		t = edge_value(tile[0])
		b = edge_value(tile[edge_max])
		l = edge_value([row[0] for row in tile])
		r = edge_value([row[edge_max] for row in tile])

		edges = (t,r,b,l) # clockwise winding
		xflip = flip_x(edges, edge_len)
		# calculate the other 4 possible rotations (a,b,c,d)
		rotations = [edges]
		for i in range(0,3):
			edges = rotate_edges(edges, edge_len)
			rotations.append(edges)
		rotations.append(xflip)
		for i in range(0,3):
			xflip = rotate_edges(xflip, edge_len)
			rotations.append(xflip)

		tile_edges[tile_id] = rotations

		#print('tile ', tile_id)
		#for r in rotations:
		#	print([bin_to_edge(x) for x in r])

		# build index of edge_id to [(tile_id, rotation_idx)...]
		# this is put in an array for each edge orientation to 
		# optimize matching
		for rot_index, rot in enumerate(rotations):
			for i in range(0,4):
				em = edge_map[i]
				entry = (tile_id, rot_index)
				if rot[i] in em:
					em[rot[i]].append(entry)
				else:
					em[rot[i]] = [entry]


	# identify corner and edge pieces
	corner_pieces = set()
	edge_pieces = set()
	for tile_id in tiles:
		adj = set()
		edges = tile_edges[tile_id]
		for edge in edges[0]:
			for em in edge_map:
				if edge in em:
					for tile in em[edge]:
						adj.add(tile[0])
		if tile_id in adj:
			adj.remove(tile_id)
		if (len(adj) == 2):
			corner_pieces.add(tile_id)
		if (len(adj) == 3):
			edge_pieces.add(tile_id)


	# print(edge_map)

	prod = 1
	for c in corner_pieces:
		prod *= c
	#return prod

	grid = [[0]*width for i in range(0, height)]
	visited = set()

	def render_grid():
		for row in grid:
			print(row)
		ts = 10
		joined = ['' for i in range(0, height*(ts - 2))]
		for y in range(0, height):
			for x in range(0, width):
				cell = grid[y][x]
				if (cell == 0):
					break
				tile = copy.deepcopy(tiles[cell[0]])
				rot = cell[1]
				ts = len(tile)

				if (rot > 3):
					for i,line in enumerate(tile):
						tile[i] = line[::-1]
					rot -= 4
					pass

				for ty in range(0, ts):
					for tx in range(0, ts):
						ax = tx
						ay = ty
						# rotate
						for i in range(0, rot):
							ax, ay = ay, (ts - 1) - ax
						if (ax != 0 and ax != ts-1 and ay != 0 and ay != ts-1):
							joined[y * (ts - 2) + (ty - 1)] += tile[ay][ax]
					#joined[y * (ts + 1) + ty] += ' '

		for row in joined:
			print(row)
		return joined

	#grid[0][0] = (1951, 9)
	#print_grid()
	## Solve

	def do_square(x, y):
		global grid, visited
		if x == 0:
			adj = grid[y-1][0]
			tid = adj[0]
			rot = adj[1]
			adj_bot = tile_edges[tid][rot][BOTTOM]
			if adj_bot in edge_map[TOP]:
				for option in edge_map[TOP][adj_bot]:
					if option[0] not in visited:
						visited.add(option[0])
						grid[y][x] = option
						if do_square(x + 1, y):
							return True
						visited.remove(option[0])
		else:
			adj_left = grid[y][x-1]
			tid_left = adj_left[0]
			rot_left = adj_left[1]
			adj_right = tile_edges[tid_left][rot_left][RIGHT]

			adj_bot = -1
			if y > 0:
				adj_top = grid[y-1][x]
				tid_top = adj_top[0]
				rot_top = adj_top[1]
				adj_bot = tile_edges[tid_top][rot_top][BOTTOM]
			if adj_right in edge_map[LEFT]:
				options = edge_map[LEFT][adj_right]
				for option in options:
					if option[0] not in visited:
						# check top edge
						if y == 0 or adj_bot == tile_edges[option[0]][option[1]][TOP]:
							new_bot = tile_edges[option[0]][option[1]]

							visited.add(option[0])
							grid[y][x] = option
							if x == (width - 1):
								if y == (height - 1):
									# solved!
									return True
								#print('y:', y)				
								#print_grid()
								if do_square(0, y + 1):
									return True
							elif do_square(x + 1, y):
								return True
							visited.remove(option[0])
		return False


	def solve_i():
		global grid, visited
		for corner in corner_pieces:
			for rot in range(0, 8):
				print("corner: ", corner, "rot: ", rot)
				visited.clear()
				visited.add(corner)
				grid[0][0] = (corner, rot)
				if do_square(1, 0):
					return True
		return False

	r = solve_i()
	image = render_grid()

	monster = [
		"                  # ",
		"#    ##    ##    ###",
		" #  #  #  #  #  #   "
	]
	slen = len(monster[0])

	cells_per_monster = 15

	def is_monster(x, y):
		roughness = 0
		for sy in range(0, 3):
			for sx in range(0, slen):
				iy = y-1+sy
				ix = x+sx
				if image[iy][ix] != '#':
					if monster[sy][sx] == '#':
						return False

		return True
	
	# identify sea monsters
	monster_count = 0
	for i in range(0, 8):
		if (i == 4):
			flip_tile(image)
		for y in range(1, len(image)-1):
			for x in range(0, len(image[0]) - slen):
				if is_monster(x, y):
					monster_count += 1
		image = rotated_tile(image)

	roughness = 0
	for row in image:
		roughness += row.count('#')

	roughness -= monster_count * cells_per_monster
	if not r:
		return 0

	# return product of the 4 corner tile_id values
	return (prod, roughness)

t1, t2 = solve(test)
print(t1)
assert(t1 == 20899048083289)

p1, p2 = solve(lines)
print('p1:', p1)
print('p2:', p2)
