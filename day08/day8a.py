import os
import copy

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]

class VM:
	def __init__(self):
		self.code = []
		self.reset()

	def reset(self):
		self.i = 0
		self.a = 0
		self.executed = set()

	def load(self, alines):
		for line in alines:
			w = line.split()
			self.code.append([w[0], int(w[1])])

	def loadstr(self, s):
		self.load(s.split('\n'))

	def run(self):
		self.i = 0
		while (self.i not in self.executed):
			self.executed.add(self.i)
			if (self.i == len(self.code)):
				return True
			op = self.op()
			self.i += getattr(self, 'op_' + op, self.panic)()
		return False

	def ins(self):
		return self.code[self.i]
	def op(self):
		return self.code[self.i][0]
	def arg(self):
		return self.code[self.i][1]
	def get_op(self, i):
		return self.code[i][0]
	def set_op(self, i, op):
		self.code[i][0] = op
	def panic(self):
		raise "PANIC at " + self.i
	
	def op_nop(self):
		return 1
	def op_acc(self):
		self.a += self.arg()
		return 1
	def op_jmp(self):
		return self.arg()

def fix(vm):
	for i in range(0, len(vm.code)):
		vm.reset()
		if (vm.get_op(i) == "nop"):
			vm.set_op(i, "jmp")
			if vm.run():
				return vm.a
			else:
				vm.set_op(i, "nop")

		elif (vm.get_op(i) == "jmp"):
			vm.set_op(i, "nop")
			if vm.run():
				return vm.a
			else:
				vm.set_op(i, "jmp")
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