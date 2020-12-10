import os

sdir = os.path.dirname(os.path.realpath(__file__))
input = [int(line) for line in open(sdir + "/input.txt").readlines()]
test_input = [int(line) for line in open(sdir + "/test.txt").readlines()]

p1 = 0
p2 = 0

def get_diffs(values):
	diffs = []
	values.sort()
	diffs.append(values[0])
	#highest = values[0]
	for i in range(1, len(values)):
		diffs.append(values[i] - values[i-1])
		#highest = max(highest, values[i])
	diffs.append(3)
	return diffs

def diff_counts(values):
	diffs = get_diffs(values)
	print(diffs)
	return diffs.count(1) * diffs.count(3)

valids = {}

def path(diffs, i):
	n = 0
	d = diffs[i]
	if i == (len(diffs) - 1):
		return 1

	if i in valids:
		return valids[i]

	for k in range(i + 1, len(diffs)):
		if (d > 3):
			break
		n += path(diffs, k)
		d += diffs[k]

	valids[i] = n
	return n

def arrangements(values):
	valids = {}
	diffs = get_diffs(values)
	return path(diffs, 0)




t = diff_counts(test_input)
print(t)
assert(t == 220)
p1 = diff_counts(input)

#t2 = arrangements(test_input)
#print("t2:",t2)
#assert(t2 == 19208)

p2 = arrangements(input)


print(p1)
print(p2)