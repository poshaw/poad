#! /usr/bin/python3
# -*- coding: utf-8 -*-

import argparse, os, signal, sys

__author__ = "Phil Shaw"
__version__ = 1.0
__copyright__ = "Copyright (c) 2012 Flogistix"

def signal_handler(signum, frame):
	"""
Handle print_exit via signals
"""
	print("\n(Terminated with signal %d)\n" % (signum))
	# do handle shutdown stuff here
	sys.exit(0)
	
def setup_signal_handler():
	signal.signal(signal.SIGINT, signal_handler) # Handle Ctrl-C
	if hasattr(signal, "SIGBREAK"):
		# Handle Ctrl-Break e.g. under Windows
		signal.signal(signal.SIGBREAK, signal_handler)

def main(args):
	setup_signal_handler() # handle Ctrl-C

	parser = argparse.ArgumentParser(description='{}'.format(__doc__))
	parser.add_argument('-v', '--verbose', action='count', help='provides more output durring execution. -vv will display even more...')
	parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
	opts = parser.parse_args()

	# define your own USEFUL output message 
	# try:
		# a = 3 / 0
	# except ZeroDivisionError as e:
		# exc_type, exc_obj, exc_tb = sys.exc_info()
		# fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
		# print("\tError: {}".format(exc_type))
		# print("\t\t{}".format(e))
		# print("\t\tIn file: {}".format(fname))
		# print("\t\tLine: {}".format(exc_tb.tb_lineno))
	# bind ValueError object to local name ex
	
	# try:
		# x = float('blah')
	# except ValueError as ex:
		# print("value exception occurred ", ex)

	# catch two different exceptions simultaneously
	try:
		x = float('blah')
	except (ValueError, NameError) as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
		print("\tError: {}".format(exc_type))
		print("\t\t{}".format(e))
		print("\t\tIn file: {}".format(fname))
		print("\t\tLine: {}".format(exc_tb.tb_lineno))
	

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))