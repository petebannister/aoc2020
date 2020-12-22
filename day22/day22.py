import os
import copy
import math

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

def load(lines):
	hands = [[],[]]
	state = 0
	for line in lines:
		if state == 0:
			state = 1
		elif state == 1:
			if line:
				hands[0].append(int(line))
			else:
				state = 2
		elif state == 2:
			state = 3
		elif state == 3:
			if line:
				hands[1].append(int(line))
			else:
				state = 4
	return hands

def pop_front(hand):
	f = hand[0]
	del hand[0]
	return f

def solve(lines):
	r1 = 0
	r2 = 0
	hands = load(lines)
	print(hands)

	winner = -1
	while winner < 0:
		p0 = pop_front(hands[0])
		p1 = pop_front(hands[1])
		if (p0 > p1):
			hands[0].append(p0)
			hands[0].append(p1)
			if 0 == len(hands[1]):
				winner = 0
		else:
			hands[1].append(p1)
			hands[1].append(p0)
			if 0 == len(hands[0]):
				winner = 1

	print("winner ", winner)

	# score. The bottom card in their deck is worth the value 
	# of the card multiplied by 1, the second-from-the-bottom 
	# card is worth the value of the card multiplied by 2, and so on.
	n = len(hands[winner])
	score = 0
	for i, c in enumerate(hands[winner]):
		score += (n - i) * hands[winner][i]

	r1 = score
	return (r1, r2)

t1, t2 = solve(test)
print('t1:', t1)
print('t1:', t2)
assert(t1 == 306)

p1, p2 = solve(lines)
print('p1:', p1)
print('p2:', p2)
