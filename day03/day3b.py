import os
#from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]

def check(right, down):
    trees = 0
    x = 0
    for y in range(0, len(lines), down):
        line = lines[y]
        dx = x % len(line)
        if (line[dx] == '#'):
            trees += 1
        x += right
    return trees

total = 1;
total *= check(1, 1)
total *= check(3, 1)
total *= check(5, 1)
total *= check(7, 1)
total *= check(1, 2)
print(total)
