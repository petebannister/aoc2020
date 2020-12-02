import os
from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
data = [line.strip() for line in open(sdir + "\\day2.txt").readlines()]
nvalid = 0
for d in data:
    (a, b, ch, pw) = parse("{:d}-{:d} {}: {}", d)
    n = (pw[a-1] + pw[b-1]).count(ch)
    if (n == 1):
        nvalid += 1
        print(pw)

print(nvalid)
