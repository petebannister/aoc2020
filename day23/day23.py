import os
import copy
import math

sdir = os.path.dirname(os.path.realpath(__file__))
#lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
#test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

def solve(input, N, iterations):
	# build data structure
	nums = [int(x) for x in input]
	cups = [i+1 for i in range(0, N + 1)]
	cups[0] = None # not used
	for i in range(1, len(input)):
		cup = int(input[i-1])
		next = int(input[i])
		cups[cup] = next
	next_fixed = len(input)+1
	current = int(input[0])
	if N == len(input):
		cups[int(input[-1])] = current
	else:
		cups[int(input[-1])] = len(input)+1
		cups[-1] = current
	for i in range(0, iterations):
		# print("move: ", N)
		# print("cups: ", cups)
		# print("current: ", current)
		a = cups[current]
		b = cups[a]
		c = cups[b]
		dest = current - 1
		if dest == 0:
			dest = N
		while dest == a or dest == b or dest == c: # in taken:
			dest -= 1
			if dest == 0:
				dest = N
				
		next = cups[c]
		cups[current] = next
		cups[c] = cups[dest]
		cups[dest] = a
		current = cups[current]
		if 0 == i & 0xFFFFF:
			print(i)

	p1 = ''
	current = 1
	for i in range(1, len(input)):
		current = cups[current]
		p1 += str(current)
	a = cups[1]
	b = cups[a]
	p2 = a * b
	return p1, p2

#ta,_ = solve("389125467", 10)
t1,_ = solve("389125467", 9, 100)
print('t1:', t1)
#print('t2:', t2)
assert(t1 == "67384529")
_,t2 = solve("389125467", 1000000, 10000000)
assert(t2 == 149245887792)

p1, _ = solve("942387615", 11, 100)
print('p1:', p1)
_,p2 = solve("942387615", 1000000, 10000000)
assert(p2 == 562136730660)
print('p2:', p2)
