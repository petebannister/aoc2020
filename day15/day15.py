import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))

data = [0,14,6,20,1,4]

def get_up_to(numbers, lim):
	times={}
	for i,n in enumerate(numbers):
		times.update({n: i})

	time = len(numbers) - 1
	n = numbers[time]
	for time in range(len(numbers)-1, lim-1):
		last = n
		if n in times:
			n = time - times[n]
		else:
			n = 0
		times.update({last:time})
		time += 1

		if (0 == time % 100000):
			print(time)
		#print(time, ", ", n)
		# 0 3 3 1 0 4 0

	return n


t = get_up_to([0,3,6], 2020)
assert(t == 436)
p1 = get_up_to(data, 2020)
assert(p1 == 257)
print(p1)
p2 = get_up_to(data, 30000000)
print(p2)
