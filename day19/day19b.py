import os
import re

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test2 = [line.strip() for line in open(sdir + "/test2.txt").readlines()]

rules = {}
pos = 0
choice = 0
choice_idx = 0

def validate_i(line, id):
	global pos, choice_idx
	if pos >= len(line):
		return False

	rule = rules[id]
	if isinstance(rule, str):
		ch = line[pos:pos+len(rule)]
		if rule == ch:
			pos += len(rule)
			return True
		return False

	for alternative in rule:
		if id == 8 or id == 11:
			recurse = 0 != (choice & (1 << choice_idx))
			choice_idx = choice_idx + 1
			if recurse:
				continue

		beg = pos
		ok = True
		for sub in alternative:
			r = validate_i(line, sub)
			if not r:
				pos = beg
				ok = False
				break
		if ok:
			return True
	return False


def validate(line):
	global pos, stack, choice, choice_idx
	pos = 0
	stack = []
	for choice in range(0, 1024):
		choice_idx = 0
		if validate_i(line, 0):
			if pos == len(line):
				return True
	return False

def solve(lines,  override_rules = {}):
	global rules
	global pos

	rules = {}
	sum = 0
	state = 0
	all = set()
	for line in lines:
		if state == 0:
			if not line: 
				state = 1
				rules.update(override_rules)

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
				print(line)
				sum += 1
			
	return sum

part2_overrides = {
	8:  [[42], [42,8]],
	11: [[42, 31], [42, 11, 31]]
}

t2 = solve(test2, part2_overrides)
print('t2:', t2)
assert(t2 == 12)

t1 = solve(test2)
print('t1:', t1)
assert(t1 == 3)


p1 = solve(lines)
print('p1:', p1)
assert(p1 == 220)
p2 = solve(lines, part2_overrides)
print('p2:', p2)
