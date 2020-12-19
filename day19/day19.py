import os
import re

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

rules = {}
pos = 0

def validate_i(line, id):
	global pos
	if pos >= len(line):
		return False
	if id not in rules: return False
	rule = rules[id]
	if isinstance(rule, str):
		ch = line[pos]
		if rule == ch:
			pos += 1
			return True
		return False

	for alternative in rule:
		beg = pos
		ok = True
		for sub in alternative:
			if not validate_i(line, sub):
				pos = beg
				ok = False
				break
		if ok:
			return True
	return False

def validate(line):
	global pos
	pos = 0
	if validate_i(line, 0):
		return pos == len(line)
	return False

def solve(lines):
	global rules
	sum = 0
	state = 0
	for line in lines:
		if state == 0:
			if not line: state = 1
			else:
				id, rt = line.split(':')
				alt = rt.strip().split('|')
				id = int(id)
				if alt[0].startswith('"'):
					rules[id] = alt[0][1]
				elif 1 == len(alt):
					rules[id] = [[int(x) for x in alt[0].split(' ')]]
				else:
					rules[id] = [
						[int(x) for x in alt[0].strip().split(' ')],
						[int(x) for x in alt[1].strip().split(' ')]
					]

		elif state == 1:
			if validate(line):
				sum += 1
			
	# print(rules)
	return sum

t = solve(test)
print(t)
assert(t == 2)

p1 = solve(lines)
print('p1:', p1)
p2 = 0 #solve(grid4(lines), 6, seq4)
print('p2:', p2)
