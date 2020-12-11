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
	return '.'

def num_occupied(board, x, y):
	adj = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
	n = 0
	for a in adj:
		if '#'==(get_cell(board, x + a[0], y + a[1])):
			n += 1
	return n

def step(board, next):
	for y in range(0, len(board)):
		row = board[y]
		for x in range(0, len(row)):
			s = row[x]
			if '#' == s:
				if 4 <= num_occupied(board, x, y):
					s = 'L'
			if 'L' == s:
				if 0 == num_occupied(board, x, y):
					s = '#'
			next[y][x] = s
					
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