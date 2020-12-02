import os
from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
data = [line.strip() for line in open(sdir + "\\day2.txt").readlines()]
#data = list(map(int, data))
nvalid = 0
for d in data:
    (a, b, ch, pw) = parse("{:d}-{:d} {}: {}", d)
    n = 0
    if (pw[a-1] == ch): n += 1
    if (pw[b-1] == ch): n += 1
    if (n == 1):
        nvalid += 1
        print(pw)

print(nvalid)
