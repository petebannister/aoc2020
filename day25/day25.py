import os
import copy
import math

sdir = os.path.dirname(os.path.realpath(__file__))
#lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
#test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

# something like DH key exchange

def bruteL(key, N):
	v = 1
	L = 0
	while v != key:
		v = (v * 7) % N
		L = L + 1
	return L

def solve(A, B):
	r1 = 0
	r2 = 0

	N = 20201227
	if A == 12092626: # found by brute force
		LA = 14775052
		LB = 12413864
	else:
		LA = bruteL(A, N)
		LB = bruteL(B, N)

	print("LA: ", LA)
	print("LB: ", LB)

	# alternatively is there a mod_pow function
	EA = pow(B, LA, N)
	EB = pow(A, LB, N)

	assert(EA == EB)

	r1 = EA
	return (r1, r2)


t1, t2 = solve(5764801, 17807724)
print('t1:', t1)
print('t1:', t2)
assert(t1 == 14897079)

p1, p2 = solve(12092626, 4707356)
print('p1:', p1)
print('p2:', p2)
