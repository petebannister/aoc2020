import os
#from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]

tot = 0
grp = 0
gs = set()
for line in lines:
	if len(line) == 0:
		tot += len(gs)
		gs = set()
	else:
		for c in line:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				gs.add(c)
				
tot += len(gs)
assert(tot != 6518)
print(tot)