import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [list(line.strip()) for line in open(sdir + "/input.txt").readlines()]
test = [list(line.strip()) for line in open(sdir + "/test.txt").readlines()]

def get_cell(board, x, y):
	if (0 <= y < len(board)):
		row = board[y]
		if (0 <= x < len(row)):
			return row[x]
	return 'X'

#def num_occupied(board, x, y):
#	adj = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
#	n = 0
#	for a in adj:
#		if '#'==(get_cell(board, x + a[0], y + a[1])):
#			n += 1
#	return n

def num_occupied_p2(board, x, y):
	adj = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
	n = 0
	for a in adj:
		pos = [x,y]
		cell = '.'
		while cell == '.':
			pos = [pos[0] + a[0], pos[1] + a[1]]
			cell = get_cell(board, pos[0], pos[1])
			if '#'== cell:
				n += 1
				break

	return n

def print_board(board):
	for row in board:
		print(''.join(row))
	print(' ')

def step(board, next):
	for y in range(0, len(board)):
		row = board[y]
		for x in range(0, len(row)):
			s = row[x]
			if '#' == s:
				if 5 <= num_occupied_p2(board, x, y):
					s = 'L'
			if 'L' == s:
				if 0 == num_occupied_p2(board, x, y):
					s = '#'
			next[y][x] = s
	#print_board(board)
def exec(board):
	next = copy.deepcopy(board)
	step(board, next)
	while board != next:
		board, next = next, board
		step(board, next)

def total_occupied(board):
	n = 0
	for y in range(0, len(board)):
		row = board[y]
		for x in range(0, len(row)):
			if row[x] == '#':
				n = n + 1
	return n

exec(test)
t = total_occupied(test)
print(t)

exec(lines)

p1 = total_occupied(lines)
p2 = 0

print(p1)
print(p2)