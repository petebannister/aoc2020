import os
sdir = os.path.dirname(os.path.realpath(__file__))
data = open(sdir + "\\day1.txt").readlines()
data = list(map(int, data))
for a in data:
    for b in data:
        if (2020 == (a + b)):
            print ("answer:", a * b)
            exit
