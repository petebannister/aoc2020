import os
from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
data = open(sdir + "\\day2.txt").readlines()
nvalid = 0
for d in data:
    (mn, mx, ch, pw) = parse("{:d}-{:d} {}: {}", d)
    nch = pw.count(ch)
    if (nch >= mn and nch <= mx):
        nvalid += 1

print(nvalid)
