import os
from enum import IntEnum
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]

class CC(IntEnum):
	nop = 0
	term = 1
	acc = 2
	jmp = 3

class Ins:
	cc = CC.term
	arg = 0
	def __init__(self, acc, aarg):
		self.cc = acc
		self.arg = aarg


class VM:
	def __init__(self):
		self.code = []
		self.reset()

	def reset(self):
		self.i = 0
		self.a = 0
		self.executed = set()

	def clone(self):
		c = VM()
		c.code = copy.deepcopy(self.code)
		c.a = self.a
		c.i = self.i
		return c

	def load(self, alines):
		for line in alines:
			w = line.split()
			self.code.append(Ins(CC[w[0]], int(w[1])))
		self.code.append(Ins(CC.term, 0))

	def loadstr(self, s):
		self.load(s.split('\n'))

	def run(self):
		i = 0
		while (self.i not in self.executed):
			self.executed.add(self.i)
			if (self.i >= len(self.code)):
				return False
			if not self.statement():
				return True
		return False
		#while self.statement():
		#	if (self.i in self.executed):
		#		return False
		#	self.executed.add(self.i)
		#return True

	def ins(self):
		return self.code[self.i]

	def statement(self):
		ins = self.ins();
		cc = ins.cc
		if (cc == CC.term):
			return False
		op = getattr(self, 'op_' + cc.name, self.op_panic)
		self.i += op()
		return True

	def op_panic(self):
		raise "PANIC at " + self.i;
	
	def op_nop(self):
		return 1

	def op_acc(self):
		self.a += self.ins().arg
		return 1

	def op_jmp(self):
		return self.ins().arg



def fix(vm):
	for i in range(0, len(vm.code)):
		vm.reset()
		if (vm.code[i].cc == CC.nop):
			vm.code[i].cc = CC.jmp 
			if vm.run():
				return vm.a
			else:
				vm.code[i].cc = CC.nop

		elif (vm.code[i].cc == CC.jmp):
			vm.code[i].cc = CC.nop
			if vm.run():
				return vm.a
			else:
				vm.code[i].cc = CC.jmp
	return 0



p1 = 0
p2 = 0

test = VM()
test.loadstr('''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6''')

print(fix(test))

vm = VM()
vm.load(lines)

vm.run()
p1 = vm.a

p2 = fix(vm)
print(p1)
print(p2)