import os
import copy
import math

sdir = os.path.dirname(os.path.realpath(__file__))
#lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
#test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

class Node:
	def __init__(self, v):
		self.next = self
		self.v = v
	def append(self, v):
		a = self.next
		self.next = Node(v)
		self.next.next = a
		return self.next

	def take3(self):
		a = self.next
		b = a.next
		c = b.next
		self.next = c.next
		c.next = None
		return a
	def find(self, v):
		node = self
		while node.v != v:
			node = node.next
			if not node:
				return None
		return node
	def insert3(self, nodes):
		after = self.next
		self.next = nodes
		nodes.next.next.next = after

lookup = {}

def move(node, N):
	taken = node.take3()
	current = node.v
	dest = current - 1
	if dest == 0:
		dest = N
	while taken.find(dest):
		dest = dest - 1
		if dest == 0:
			dest = N

	# TODO: lookup
	dest_node = lookup[dest] #node.find(dest)
	dest_node.insert3(taken)
	return node.next

def cups_after_1(node):
	node = node.find(1)
	return v[ni+1:] + v[:ni]

def to_list(node):
	r = []
	n = node
	while True:
		r.append(n.v)
		n = n.next
		if n == node:
			break
	return r;


def solve(input, iterations):
	global lookup
	r1 = 0
	r2 = 0

	N = 1
	lookup = {}
	cups = Node(int(input[0]))
	lookup[cups.v] = cups
	c2 = cups
	for i in range(1, len(input)):
		c2 = c2.append(int(input[i]))
		lookup[c2.v] = c2

	current = cups
	for i in range(0, iterations):
		# print("move: ", N)
		# print("cups: ", cups)
		# print("current: ", current)
		current = move(current, len(input))
		N = N + 1
		# print('')
	print("final: ", to_list(cups))
	t = lookup[1]
	a = t.next.v
	b = t.next.next.v
	print('a', a)
	print('b', b)
	r1 = a * b
	#r1 = 0 # ''.join([str(x) for x in cups_after_1(cups)])

	lookup = {}
	cups = Node(int(input[0]))
	lookup[cups.v] = cups
	c2 = cups
	for i in range(1, len(input)):
		c2 = c2.append(int(input[i]))
		lookup[c2.v] = c2

	max_N = 1000000
	for x in range(10, max_N+1):
		c2 = c2.append(x)
		lookup[c2.v] = c2

	current = cups
	for i in range(0, (max_N * 10)):
		current = move(current, max_N)
		N = N + 1
		#print(part_b[:30])
		if (0 == N % 10000):
			print(N)
			
			t = lookup[1]
			a = t.next.v
			b = t.next.next.v
			print('a', a)
			print('b', b)

	t = lookup[1]
	a = t.next.v
	b = t.next.next.v
	print('a', a)
	print('b', b)
	r2 = a * b
	return (r1, r2)



#ta,_ = solve("389125467", 10)
t1,t2 = solve("389125467", 100)
print('t1:', t1)
print('t2:', t2)
#assert(t1 == "67384529")
assert(t2 == 149245887792)

p1, p2 = solve("942387615", 100)
print('p1:', p1)
print('p2:', p2)
