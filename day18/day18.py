import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
#test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

stack = []
str = ''
pos = 0

# Recursive descent parser

def cur():
	global pos, str, stack
	if (pos >= len(str)):
		return ''
	return str[pos]

def expect(v):
	global pos, str, stack
	if not v:
		raise "Expectation failure at " + pos

def group():
	global pos, str, stack
	skip()
	if cur() == '(':
		pos += 1
		expression()
		skip()
		assert(cur() == ')')
		pos += 1
		return True
	return False

def skip():
	global pos, str, stack
	while cur() == ' ':
		pos += 1

def number():
	global pos, str, stack
	skip()
	num = ''
	while cur().isdigit():
		num += cur()
		pos += 1
	if len(num):
		stack.append(int(num))
		return True
	return False

def term():
	return group() | number()

def accept(op):
	global pos, str, stack
	if (cur() == op):
		pos += 1
		return True
	return False

def multiply():
	global pos, str, stack
	skip()
	if (accept('*')):
		expect(term())
		b = stack.pop()
		a = stack.pop()
		stack.append(a * b)
		return True
	return False

def plus():
	global pos, str, stack
	skip()
	if (accept('+')):
		expect(term())
		b = stack.pop()
		a = stack.pop()
		stack.append(a + b)
		return True
	return False



def expression():
	if term():
		while multiply() | plus():
			pass
		return True
	return False

def solve_line(line):
	global pos, str, stack
	str = line
	pos = 0
	stack = []
	expression()
	return stack.pop()


def solve(lines):
	sum = 0
	for line in lines:
		if line:
			sum += solve_line(line)
	return sum

t = solve_line('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
print(t)
assert(t == 13632)

p1 = solve(lines)
print('p1:', p1)
p2 = 0 #solve(grid4(lines), 6, seq4)
print('p2:', p2)
