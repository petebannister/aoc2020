import os
from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
data = open(sdir + "\\day2.txt").readlines()
#data = list(map(int, data))
nvalid = 0
for d in data:
    (mn, mx, ch, pw) = parse("{}-{} {}: {}", d)
    (mn, mx, ch, pw) = (int(mn), int(mx), ch[0], pw)
    nch = pw.count(ch)
    if (nch >= mn and nch <= mx):
        nvalid += 1

print(nvalid)
