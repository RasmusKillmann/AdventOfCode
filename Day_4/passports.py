import re


# -- Vars. --
file_input = 'input.txt'
passports  = []
counter    = 0

# -- Open File --
with open(file_input, encoding='utf-8') as file:
    contents = file.read()
    inputs    = contents.split('\n\n')

# -- List to Dict. --
for index, i in enumerate(inputs):
    data     = i.replace('\n',' ').split()
    details  = [i.split(':') for i in data]
    dict     = {x[0]:x[1] for x in details}
    passports.append(dict)


#-- Validators --

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def byr(byr):
	return int(byr)<=2002 and int(byr) >=1920

def iyr(iyr):
	return int(iyr)<=2020 and int(iyr)>= 2010


def eyr(eyr):
	return int(eyr)<=2030 and int(eyr)>= 2020

def hgt(hgt):
	return (hgt[-2:]=='cm' and int(hgt[:-2])>=150 and int(hgt[:-2])<=193) or (hgt[-2:]=='in' and int(hgt[:-2])>=59 and int(hgt[:-2])<=76)

def hcl(hcl):
	return hcl[0]=='#' and len(hcl[1:])==6 and re.match("([a-f]*[0-9]*)*",hcl[1:])

def ecl(ecl):
	return ecl == 'amb' or ecl=='blu' or ecl=='brn' or ecl=='gry' or ecl=='grn' or ecl=='hzl' or ecl=='oth'

def pid(pid):
	return re.match("[0-9]*", pid) and len(pid)==9

for index, x in enumerate(passports):
	keys = x.keys()
	if all(field in keys for field in fields):
		if all([byr(x['byr']), iyr(x['iyr']), eyr(x['eyr']), hgt(x['hgt']), hcl(x['hcl']), ecl(x['ecl']), pid(x['pid'])]):
			counter+=1

print(counter)