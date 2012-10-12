#! /usr/bin/python3
#coding=utf-8

__author__ = "Phil Shaw"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2012/07/08$"
__copyright__ = "Copyright (c) 2012 Phil Shaw"
__license__ = "Python"

import getopt, sys

# global variables
verbose = False
output_file = None

def main(args):
	global verbose, output_file
	#handle command line arguments
	def usage():
		print("""\n
usage: {:s} [options] 
	-h, --help	: Display help and exit
	-o, --output_file=	: specify output_file file
	-v		: verbose output_file
""".format(sys.argv[0])) # looks good on windows have to check linux
             
	try:
		opts, args = getopt.getopt(args, "ho:v", ["help", "output_file="])
	except getopt.GetoptError as err:
		# print help information and exit:
		print(err) # will print something like "option -a not recognized"
		usage()
		return 2# sys.exit(2)
	
	for o, a in opts:
		if o == "-v":
			verbose = True
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-o", "--output_file"):
			output_file = a
			# only print if verbose tag is enabled
			if verbose:
				print("output file = {:s}".format(output_file))
		else:
			assert False, "unhandled option"
	if verbose:
		print("argv = {}".format(sys.argv[1:]))
		print('options   : {}'.format(opts))
		print("extra arguments: {}".format(args))
	
	# program starts here
	
	# if no argument was passed ask user for input
	if len(args) == 0:
		try:
			radius = float( input("enter radius: "))
		except ValueError as e:
			print("error:", e)
			return 2
	# use command line argument for calculation
	else:
		try:
			radius = float(args[0])
		except ValueError as e:
			print("error:", e)
			return 2
	import math
	print("The area is {0:.2f}".format( math.pi * radius**2))
	return 0

if __name__ == "__main__":
	import sys
	sys.exit(main(sys.argv[1:]))