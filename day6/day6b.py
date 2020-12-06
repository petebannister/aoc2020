import os
#from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]

tot = 0
ngrp = 0
gs = [0]*26

for line in lines:
	if len(line) == 0:
		tot += gs.count(ngrp)
		# tot += len(gs)
		gs = [0]*26
		ngrp = 0
	else:
		ngrp += 1
		for c in line:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				gs[ord(c) - ord('a')] += 1
				
tot += gs.count(ngrp)
#assert(tot != 6518)
print(tot)