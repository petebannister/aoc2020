import os
#from parse import parse

sdir = os.path.dirname(os.path.realpath(__file__))
lines = [line.strip() for line in open(sdir + "/input.txt").readlines()]
nvalid = 0
passport = {}


optional = { 'cid' }

required = {  
	'byr',
	'iyr',
	'eyr',
	'hgt',
	'hcl',
	'ecl',
	'pid' }

def validate(passport):
	if (len(required) == len(required & passport.keys())):
		return 1
	else:
		return 0

for line in lines:
	fields = [field.strip() for field in line.split(' ') if (0 != len(field.strip()))]
	if len(fields) == 0:
		nvalid += validate(passport)
		passport = {}
	else:
		for field in fields:
			parts = field.split(':')
			kvp = {parts[0]: parts[1]}
			passport.update(kvp)
			
nvalid += validate(passport)

print(nvalid)
