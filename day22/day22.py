import os
import copy
import math

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]


def solve(lines):
	r1 = 0
	r2 = 0

	items = []
	for line in lines:
		items.append(line.split(' '))

	return (r1, r2)

t1, t2 = solve(test)
print('t1:', t1)
print('t1:', t2)
assert(t1 == 5)

p1, p2 = solve(lines)
print('p1:', p1)
print('p2:', p2)
