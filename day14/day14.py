import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
#lines = [line.strip() for line in open(sdir + "/test.txt").readlines()]


mask_and = 0
mask_or = 0
mask_floating = 0
mem = {}
mem2 = {}
dmac = []

for line in lines:
	ins, val = [term.strip() for term in line.split('=')]
	if ins == 'mask':
		mask_and = 0
		mask_or = 0
		addr_mask_and = 0
		addr_mask_or = 0
		dmac = []
		for i, ch in enumerate(val):
			mask_and <<= 1
			mask_or <<= 1
			addr_mask_or <<= 1
			addr_mask_and <<= 1
			if (ch == '1'):
				mask_and += 1
				mask_or += 1
				addr_mask_or += 1
				addr_mask_and += 1
			elif (ch == '0'):
				addr_mask_and += 1
			else:
				mask_and += 1

			if (ch == 'X'):
				dmac.append(35 - i)

	elif str(ins).startswith('mem'):
		index = int(ins.split('[')[1].split(']')[0])
		val = int(val)
		modval = (val & mask_and) | mask_or
		mem[index] = modval		

		# pt 2
		addr = (index & addr_mask_and) | addr_mask_or
		for k in range(0, 1 << len(dmac)):
			dynamic_mask = 0
			for bit in range(0, len(dmac)):
				if 0 != (k & (1 << bit)):
					dynamic_mask |= (1 << dmac[bit])
			a = addr | dynamic_mask
			mem2[a] = val

p1 = sum(mem.values())
p2 = sum(mem2.values())
print(p1)
print(p2)

assert(p1 == 15172047086292)
assert(p2 != 359196893820312)
assert(p2 != 440312505658016)