import os
import copy
import math

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

def load(lines):
	items = []
	for line in lines:
		names, allergens = line.split('(contains ')
		names = set(names.strip().split())
		allergens = allergens.split(')')[0].split(', ')
		items.append((names,allergens))
	return items

def solve(lines):
	items = load(lines)
	allergens = {}
	confirmed = {}
	confirmed_lut = {}
	names = set()
	for i, item in enumerate(items):
		names.update(item[0])
		for allergen in item[1]:
			if allergen in allergens:
				allergens[allergen].append(i)
			else:
				allergens[allergen] = [i]
	allergen_set = set(allergens.keys())
	while 0 != len(allergens):
		for a in allergens:
			matches = []
			for recipe in allergens[a]:
				matches.append(copy.deepcopy(items[recipe][0]))
			for i in range(1, len(matches)):
				matches[0].intersection_update(matches[i])

			matches[0] = matches[0].difference(confirmed.keys())
			#for c in confirmed:
			#	if c in matches[0]:
			#		matches[0].remove(c)
			if 1 == len(matches[0]):
				name = next(iter(matches[0]))
				confirmed[name] = a
				confirmed_lut[a] = name
				del allergens[a]
				break # probably invalidated iteration

	# which items are not allergens
	not_allergens = names.difference(set(confirmed.keys()))
	count = 0
	for item in items:
		for name in item[0]:
			if name in not_allergens:
				count += 1

	danger_allergen = list(allergen_set)
	danger_allergen.sort()
	danger = [confirmed_lut[a] for a in danger_allergen]
	danger = ','.join(danger)
	return (count, danger)

t1, t2 = solve(test)
print(t1)
print(t2)
assert(t1 == 5)

p1, p2 = solve(lines)
print('p1:', p1)
print('p2:', p2)
