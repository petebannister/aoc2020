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

def validHeight(v):
	v = str(v);
	if (v.endswith('cm')):
		return (150 <= int(v.split('cm')[0]) <= 193)
	elif (v.endswith('in')):
		return (59 <= int(v.split('in')[0]) <= 76)

	return False


def validColour(v):
	v = str(v);
	if v.startswith('#'):
		v = v[1:]
		if (6 == len(v)):
			return all(c in "0123456789abcdef" for c in v)
	return False
	
def validate(p):
	if (len(required) != len(required & p.keys())):
		return 0
	elif (
		(1920 <= int(p['byr']) <= 2002) and
		(2010 <= int(p['iyr']) <= 2020) and
		(2020 <= int(p['eyr']) <= 2030) and
		validHeight(p['hgt']) and
		validColour(p['hcl']) and
		(p['ecl'] in { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }) and
		((len(p['pid']) == 9) and p['pid'].isdigit())):
		return 1
	return 0
		
#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.

test = {
	'pid':'087499704', 'hgt':'74in', 'ecl':'grn', 'iyr':'2012', 'eyr':'2030', 'byr':'1980',
	'hcl':'#623a2f'
}

assert(validate(test))

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
