#! /usr/bin/python3

r"""
This is the docstring
for the file.

run using:
$ python3 argument_options.py -vv 5
"""

import argparse, sys

__author__ = "Phil Shaw"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2012 Phil Shaw"
__license__ = "GPL"




def main(args):
	# define and process command options
	parser = argparse.ArgumentParser(description='{}'.format(__doc__))
	parser.add_argument('-v', '--verbose', action='count', help='provides more output durring execution. -vv will display even more...')
	parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
	parser.add_argument('-f', '--foo', action='store_true', help='an extra argument for reference') # foo is bool
	parser.add_argument('bar', type=int, help='an extra argument for reference')
	opts = parser.parse_args()

	if opts.verbose:
		print("verbose")

	if opts.verbose:
		if opts.verbose > 1:
			print("very verbose")

	if opts.foo:
		print("foo")

	print(len(args))
	print(args)
	print(opts.bar, type(opts.bar))

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
