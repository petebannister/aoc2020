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

def append_hand(winner, p0, p1, hands):
	if winner == 0:
		hands[winner].append(p0)
		hands[winner].append(p1)
		if 0 == len(hands[1]):
			return winner
	if winner == 1:
		hands[winner].append(p1)
		hands[winner].append(p0)
		if 0 == len(hands[0]):
			return winner
	return -1

def append_winner(p0, p1, hands):
	winner = -1
	if (p0 > p1):
		winner = append_hand(0, p0, p1, hands)
	else:
		winner = append_hand(1, p0, p1, hands)
	return winner

visited = set()

def deal(hands):
	return (
		pop_front(hands[0]),
		pop_front(hands[1]))

def recursive_combat(hands):
	global visited
	memo = str(hands)
	if (memo in visited):
		return 0 # player 0 wins if hands seen before
	visited.add(memo)

def calc_score(hand):
	n = len(hand)
	r = 0
	for i, c in enumerate(hand):
		r += (n - i) * hand[i]
	return r


def solve(lines):
	r1 = 0
	r2 = 0
	hands = load(lines)
	print(hands)

	winner = -1
	while winner < 0:
		p0, p1 = deal(hands)
		winner = append_winner(p0, p1, hands)

	print("winner ", winner)

	r1 = calc_score(hands[winner])

	return (r1, r2)

t1, t2 = solve(test)
print('t1:', t1)
print('t1:', t2)
assert(t1 == 306)
assert(t2 == 291)

p1, p2 = solve(lines)
assert(p1 == 32083)
print('p1:', p1)
print('p2:', p2)
