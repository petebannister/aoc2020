import os

sdir = os.path.dirname(os.path.realpath(__file__))
input = [int(line) for line in open(sdir + "/input.txt").readlines()]
test_input = [int(line) for line in open(sdir + "/test.txt").readlines()]

p1 = 0
p2 = 0

def find_valid(depth, values, i):
	v = values[i]
	for ia in range(i-1, i-(depth + 1), -1):
		a = values[ia]
		if a < v: # optimization
			for ib in range(ia-1, i-(depth + 1), -1):
				b = values[ib]
				if v == (a + b):
					return True
	return False

def find_weakness(depth, values):
	for i in range(depth, len(values)):
		if not find_valid(depth, values, i):
			v = values[i]
			return v;
	return 0

def find_sum_range(value, values):
	for i in range(len(values)-1, -1, -1):
		v = values[i]
		vmax = v
		vmin = v
		sum = v
		for k in range(i - 1, -1, -1):
			v = values[k]
			vmax = max(vmax, v)
			vmin = min(vmin, v)
			sum += v
			if (sum > value):
				break
			if (sum == value):
				return vmax + vmin


t = find_weakness(5, test_input)
tx = find_sum_range(t, test_input)
print(t)
print(tx)
assert(t == 127)
assert(tx == 62)

p1 = find_weakness(25, input)
p2 = find_sum_range(p1, input)

print(p1)
print(p2)