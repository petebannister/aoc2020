import os
import copy
import math

sdir = os.path.dirname(os.path.realpath(__file__))
#lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
#test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

def move(input, current):
	index = input.find(current)
	three = ''
	res = ''

	if (index + 4 <= len(input)):
		three = input[index + 1:index + 4]
		res = input[:index+1]+input[index+4:]
	else:
		b = (index + 4) % len(input)
		three = input[index + 1:]+input[:b]
		res = input[b:index+1]
	assert(len(three) == 3)

	print("pick up: ", three)

	dest = int(current)
	didx = -1
	while didx < 0:
		dest = dest - 1
		if (dest <= 0): # 0 not in either input
			dest = 9
		didx = res.find(str(dest))
		
	print("destination: ", dest)
	res = res[:didx+1] + three + res[didx+1:]

	# current cup must retain its index
	ni = res.find(current)
	right = res[ni+1:] + res[:ni]
	split = len(right)-index
	if split == 0:
		res = right + current
	else:
		res = right[split:] + current + right[:split]

	return res

def cups_after_1(v):
	ni = v.find('1')
	return v[ni+1:] + v[:ni]


def solve(input, iterations):
	r1 = 0
	r2 = 0

	N = 1
	input = copy.deepcopy(input)
	current = input[0]
	for i in range(0, iterations):
		print("move: ", N)
		print("cups: ", input)
		print("current: ", current)
		input = move(input, current)
		cidx = input.find(current)
		current = input[(cidx+1) % len(input)]
		N = N + 1
		print('')
	print("final: ", input)

	r1 = cups_after_1(input)
	return (r1, r2)



ta,_ = solve("389125467", 10)
tb,_ = solve("389125467", 100)
print('ta:', ta)
print('tb:', tb)
assert(ta == "92658374")
assert(tb == "67384529")

p1, p2 = solve("942387615", 100)
print('p1:', p1)
print('p2:', p2)
