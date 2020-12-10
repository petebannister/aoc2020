import os
#from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
trees = 0
x = 0
for line in lines:
    dx = x % len(line)
    if (line[dx] == '#'):
        trees += 1
    x += 3

print(trees)
