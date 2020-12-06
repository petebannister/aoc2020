import os
#from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]

tot = 0
grp = 0
gs = set()
for line in lines:
	if not line:
		tot += len(gs)
		gs = set()
	else:
		for c in line:
			gs.add(c)
				
tot += len(gs)
print(tot)