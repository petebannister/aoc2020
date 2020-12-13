import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

def shortest_wait(input):
	ts = int(input[0])
	buses = input[1].split(',')
	min_wait = ts
	best_bus = 0
	for bus in buses:
		if bus == 'x':
			continue
		bus = int(bus)
		wait = (ts + (bus-1)) // bus
		wait = (wait * bus) - ts
		if (wait < min_wait):
			min_wait = wait
			best_bus = bus
	return (best_bus, min_wait)

def part1(input):
	bus, wait = shortest_wait(input)
	return wait * bus

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
	return (a * b) // gcd(a, b)


def test_p2(buses, timestamp):
	for i in range(0,len(buses)):
		bus = buses[i]
		if bus != 'x':
			bus = int(bus)
			if (0 != ((timestamp + i) % bus)):
				return False
	return True

def part2(input):
	buses = input[1].split(',')
	m = 1
	assert(buses[0] != 'x')
	period = int(buses[0])
	offset = 0
	for i in range(1,len(buses)):
		bus = buses[i]
		if bus == 'x':
			continue
		bus = int(bus)
		for k in range(1, bus):
			if 0 == (((k * period) + (offset + i)) % bus):
				offset += k * period
				period = lcm(period, bus)
				print("period: ", period)
				print("offset: ", offset)
				break

	print("offset:", offset)

	assert(test_p2(buses, offset))
	return offset


t = part1(test)
print(t)
assert(t == 295)

t2 =part2(test)
print(t2)
assert(t2 == 1068781)

p1 = part1(lines)
p2 = part2(lines)

print(p1)
print(p2)