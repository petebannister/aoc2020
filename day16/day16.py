import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]
test2 = [line.strip() for line in open(sdir + "/test2.txt").readlines()]

p1 = 0
p2 = 0

def solve(input, fieldname):
	rules = []
	yours = []
	nearby = []
	valid = []
	state = 0
	for line in input:
		if (line):
			if state == 0:
				name, rule_str = line.split(':')
				a, b = rule_str.strip().split(' or ')
				aa, ab = a.split('-')
				ba, bb = b.split('-')
				rule = [name, (int(aa), int(ab)), (int(ba), int(bb))]
				rules.append(rule)
			elif state == 1:
				state += 1
			elif state == 2:
				yours = [int(field) for field in line.split(',')]
			elif state == 3:
				state += 1
			elif state == 4:
				ticket = [int(field) for field in line.split(',')]
				nearby.append(ticket)
		else:
			state += 1
	#print(rules)
	#print(yours)
	#print(nearby)

	p1 = 0
	valid.append(yours) # assume your ticket is also valid
	for ticket in nearby:
		valid_ticket = True
		for field in ticket:
			invalid = True
			for rule in rules:
				if ((rule[1][0] <= field <= rule[1][1]) or
					(rule[2][0] <= field <= rule[2][1])):
					invalid = False
					break
			if invalid:
				p1 += field
				valid_ticket = False
		if valid_ticket:
			valid.append(ticket)
	ruleset = [i for i in range(0, len(rules))]
	applicable = [copy.deepcopy(ruleset) for i in range(0, len(yours))] # field => rules
	for ticket in valid:
		for i, field in enumerate(ticket):
			bad = []
			for k, irule in enumerate(applicable[i]):
				rule = rules[irule]
				if not ((rule[1][0] <= field <= rule[1][1]) or
					(rule[2][0] <= field <= rule[2][1])):
					bad.append(k)
			# remove any rules that dont apply
			for b in bad[::-1]: # reverse iterate to avoid index invalidation
				del applicable[i][b]

	# additional constraints which are unique
	used_rules = set();
	done = False
	while not done:
		done = True
		for i, applicable_rules in enumerate(applicable):
			if (len(applicable_rules) == 1):
				used_rules.add(applicable_rules[0])
			elif len(applicable_rules) != 0:
				done = False
				for k in range(len(applicable_rules), 0, -1):
					if applicable_rules[k-1] in used_rules:
						del applicable_rules[k-1]

	p2 = 1
	for i, applicable_rules in enumerate(applicable):
		assert(len(applicable_rules) == 1)
		rule = rules[applicable_rules[0]]
		if rule[0].startswith(fieldname):
			p2 *= yours[i]

	return (p1, p2)

t1, _ = solve(test, 'class')
_, t2 = solve(test2, 'class')
print(t1)
print(t2)
assert(t1 == 71)
assert(t2 == 12)

p1, p2 = solve(lines, 'departure')

print('p1:', p1)
print('p2:', p2)
