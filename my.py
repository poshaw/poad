#! /usr/bin/python3
#coding=utf-8

import math, os, sys

# check if 2 floats are close
def close(x, y, epsilon = 1e-7):
	return abs(x-y) < epsilon

# clear screen
def cls():
	os.system(['clear','cls'][os.name == 'nt'])

def compare(x, y):
	"""
compare handles both strings and numbers
x < y returns -1 ; x == y returns 0 ; x > y returns 1
to ignore case use:  function.compare("ABC".upper(),"abc".upper() )
"""
	if num(x) and num(y):
		if x > y:
			return 1
		if x == y:
			return 0
		if x < y:
			return -1
	elif isinstance(x, str) and isinstance(y, str):
		length = min( len(x) , len(y) ) # compare the strings up to the length of the shorter of the 2
		i = 0
		while i < length:
			if x[i] > y[i]:
				return 1
			elif x[i] < y[i]:
				return -1
			i += 1

		if len(x) == len(y): #now if string lengths are equal then we have a match
			return 0
		elif len(x) < len(y): # otherwise the shorter of the 2 strings is the smaller
			return -1
		else:
			return 1

# not finnished
def cprint(*arg):
	"""
	prints compatible to 2.7 or 3.2
	"""
	if sys.version_info[:2] == (3,2):
		print(3.2)
	elif sys.version_info[:2] == (2,7):
		print(2.7)

# golden ratio
golden_ratio = (1 + math.sqrt(5) ) / 2

# turns base 16 to base 10
def hex2dec(x):
	if isinstance(x, bytes):
		x = x.decode("utf-8")
	if isinstance(x, str):
		return int(x, 16)
	if isinstance(x, int):
		return int(x)

# makes a string into a number (int or float)
def num(s):
	try:
		assert isinstance(s, str)
		return int(s)
	except AssertionError:
		return None
	except ValueError:
		try:
			return float(s)
		except ValueError:
			return None

# return decimal answer of 2s compliment of negative binary number
def twoscompliment(x, digits):
	return int(str(x),16) ^ int("f"*digits,16)

def unbyte(x):
	x = binascii.a2b_hex(x)
	return binascii.b2a_hex(x).decode("utf-8")

# remove duplicates from a list while preserving order
def unique(items):
	found = set() # empty set
	keep = [] # empty list
	add = found.add # moved these outside the for loop to minimize external calls
	app = keep.append
	for item in items:
		if item not in found:
			add(item)
			app(item)
	return keep

############################################################

def test_close():
	print("testing close():", end='')
	x = 0.0
	numIters = 10000
	for i in range(numIters):
		x += 0.1
	x = x * 10 # to get x ≅ to numIters
	assert x != numIters
	assert close(x, numIters)
	print("\tPASSED close()")

def test_compare():
	print("testing compare():", end='')
	print(help(compare))
	print("\tPASSED compare()")

def test_hex2dec():
	print("testing hex2dec():", end='')
	assert hex2dec("f") == 15
	assert hex2dec(0xab) == 171
	assert hex2dec(b'ff') == 255
	print("\tPASSED hex2dec()")

def test_num():
	print("testing num():", end='')
	assert num(b"x") == None
	assert num("xx") == None
	assert num("6") == 6
	assert close(num("52.2"), 52.2)
	print("\t\tPASSED num()")

def test_unique():
	print("testing unique():", end='')
	L = [3, 2, 1, 2, 4, 2, 5]
	uL = unique(L)
	assert(uL == [3, 2, 1, 4, 5])
	assert(uL != [1, 2, 3, 4, 5])
	print("\tPASSED unique()")

def tests():
	test_close()
	test_compare()
	test_hex2dec()
	test_num()
	test_unique()

############################################################

def main(args):
	tests()

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
