import os
#from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]

tot = 0
grp = 0
parents = {}
prods = {}
counts = {}

for line in lines:
	parent, production = line.split(" bags contain ")
	for prod in production.split(", "):
		n, bag = prod.split(' ',1)
		if n == 'no':
			break
		else:
			n = int(n)
			if bag.endswith(' bag'):
				bag = bag[:-4]
			if bag.endswith(' bag.'):
				bag = bag[:-5]
			if bag.endswith(' bags'):
				bag = bag[:-5]
			if bag.endswith(' bags.'):
				bag = bag[:-6]
			if bag in parents:
				parents[bag].append(parent)
			else:
				parents[bag] = [parent]

			if (parent not in prods):
				prods[parent] = [bag]
				counts[parent] = [n]
			else:
				prods[parent].append(bag)
				counts[parent].append(n)


can_be_in = set()
def parent_traverse(bag):
	print(bag)
	if (bag in parents):
		for p in parents[bag]:
			if (p not in can_be_in):
				can_be_in.add(p)
				parent_traverse(p)
parent_traverse('shiny gold')
print(can_be_in)
p1 = len(can_be_in)

def child_sum(bag):
	n = 0
	if (bag in prods):
		for i in range(0, len(prods[bag])):
			c = counts[bag][i]
			contains = 1 + child_sum(prods[bag][i])
			n += contains * c
	return n
p2 = child_sum('shiny gold')

assert(p1 < 637)
print(p1)
print(p2)