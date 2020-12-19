import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
#test = [line.strip() for line in open(sdir + "/test.txt").readlines()]

# Recursive descent parser
stack = []
str = ''
pos = 0

# Lexer
def cur():
	if (pos >= len(str)): return ''
	return str[pos]
def skip():
	global pos
	while cur() == ' ': pos += 1
def pop():
	global stack
	return stack.pop()
def push(v):
	global stack
	return stack.append(v)
def accept(op):
	global pos
	skip()
	if (cur() != op): return False
	pos += 1
	return True
def expect(v):
	if not accept(v): raise "Expected '" + v + "' failure at " + pos
def expect_term():
	if not term(): raise "Expected term at " + pos
def number():
	global pos
	skip()
	num = ''
	while cur().isdigit():
		num += cur()
		pos += 1
	if 0 == len(num): return False
	push(int(num))
	return True

# Grammar / parser:
def expression():
	if not term(): return False
	while multiply(): pass
	return True
def term():
	if not factor(): return False
	while plus(): pass
	return True
def factor():
	return group() or number()
def group():
	if not accept('('): return False
	expression()
	expect(')')
	return True	
def multiply():
	if not accept('*'): return False
	expect_term()
	push(pop() * pop())
	return True
def plus():
	if not accept('+'): return False
	expect_term()
	push(pop() + pop())
	return True
def evaluate(line):
	global pos, str, stack
	str = line
	pos = 0
	stack = []
	expression()
	return pop()

def solve(lines):
	sum = 0
	for line in lines:
		if line: sum += evaluate(line)
	return sum

t = evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
print(t)
assert(t == 23340)

p2 = solve(lines)
print('p2:', p2)

