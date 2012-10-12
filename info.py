#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys, time

# #directory stuff
# # here are 2 ways to see what system we are on...
# print(os.name)
# print(sys.platform)
# print(os.getcwd()) # prints current working directory
# print(os.environ) # lots of good environment variables
# print(os.environ['USERPROFILE']) # my home folder
# print(os.getpid()) # return PID of current process
# print(os.path.basename(__file__)) # prints only script name
# print("file = {}".format( os.path.abspath( __file__ ))) # prints file with full path
# print("this platform uses \" {} \" as it's separators for pathname components".format(os.sep))
# n=5
# print("a string of {} random bytes suitable for cryptographic use: {}".format(n, os.urandom(n)))



# # lambda inline function:
# import math
# square_root = lambda x: math.sqrt(x)
# print("square root of 8 is: {}".format(square_root(8)))

# # regular expressions
# import re, string
# def inthere(aa,bb):
	# if re.search(aa, bb):
		# print("{} is in {}".format(aa, bb))
	# else:
		# print("{} is not in {}".format(aa, bb))
# str1 = 'abcdefg'
# reg = '^b'
# inthere(reg, str1)
# reg= '^a'
# inthere(reg, str1)
# mylist = ["phil", "shaw", "hello"]
# reg = 'hel'
# for x in mylist:
	# inthere(reg, x)
# consonants = string.ascii_lowercase
# vowels = 'aeiou'
# for x in vowels:
	# consonants = re.sub(x, "", consonants)
# print("consonants = {}".format(consonants))

# # import a module in a specific location
# import sys
# sys.path.append( "/home/phil/Documents/prog/python/learning/" )
# import function
# num = 2
# print("is {} even?  {}".format(num, function.isEven(num)))

# # file io stuff
# L = []
# with open('email_list.txt', 'r', encoding='utf-8-sig') as myfile:
	# for line in myfile:
		# L.append(line)
# print(L)
# # this does same thing
# f = open(input_file, 'r')
# L = f.readlines()
# f.close()

# # list stuff
# l1 = [0] * 10 # create a list with 10 elements all set to zero:
# l1 = ["0", "1", "2", "3"] # create a list directly:
# # or better yet:
# from fib import *
# f = Fib()
# l3 = [str(f.get_fib(c)) for c in range(10)]
# # create a 2d array with all elements initialized to none
# self.s = [[None for m in range(self.order)] for n in range(self.order)]
# print(' '.join(str(x) for x in l3)) # prints list with no [ or ,
# # this does the same on one line
# print(' '.join(str(x) for x in [str(f.get_fib(c)) for c in range(20)]))
# l1.pop() # remove last element:
# l1.append("item") # insert at last element:
# l1[1] = 55
# print(l1)
# l1 = [1,3,2,5,4,2,2,2,5,5,5,2]
# print(l1)
# l2 = list(set(l1)) #removes duplicates but does not preserve order
# print(l2)
# from my import *
# l2 = unique(l1) # removes duplicates, preserves order
# print(l2)
# l1 = ['a', 'b', 'c']
# l2 = [1, 2, 3]
# l3 = l1 + l2 # join 2 lists
# print("l1 + l2 = {}".format(l3)) # join 2 lists
# print('\t'.join(str(x) for x in l1)) # prints list with no [ or ,

# # argument echo
# import sys
# try:
	# for arg in sys.argv:
		# print(arg)
# except:
	# print("no arguments")

# # call another program
# import shlex, subprocess
# lcall = ['ls', '-l', 'info.py']
# subprocess.call(lcall)
# # this will tell you what your list should be to subprocess.call()
# command_line = input("Enter a command line program call: ")
# print(shlex.split(command_line))

# # user input
# try:
	# x=int(input("enter an integer"))
	# if x%2 == 0:
		# print("{} is even".format(x))
	# else:
		# print("{} is odd".format(x))
# except ValueError as e:
	# print(e)

# # decimal stuff
# import decimal
# d1 = round(decimal.Decimal('0.70') * decimal.Decimal('1.05'), 2)
# print("decimal 0.7 * 1.05 is: {}".format(d1))
# f1 = round(.70 * 1.05, 2)
# print("float   0.7 * 1.05 is: {}".format(f1))
# d2 = sum([decimal.Decimal('0.1')]*10) == decimal.Decimal('1.0')
# print("decimal .1 * 10 == 1.0: {}".format(d2))
# f2 = sum([0.1]*10) == 1.0
# print("float   .1 * 10 == 1.0 {}".format(f2))
# decimal.getcontext().prec = 36 # set precision to 36
# print(decimal.Decimal(1) / decimal.Decimal(7))

# # fraction stuff
# from fractions import Fraction
# x = Fraction(1,3)
# y = Fraction(4,6)
# print("x = " + str(x))
# print("y = " + str(y))
# ans = x + y
# print("x + y = " + str(ans))
# print("x to float: " + str(float(x)))
# f = 2.5
# z = Fraction(*f.as_integer_ratio())
# print(z)

# # random stuff
# import random
# print(random.random())  # prints a random number between 0 & 1
# print(random.randint(1,10))  #prints a random intiger between 1 & 10
# VOWELS = 'aeiou'
# x = VOWELS[random.randrange(0,len(VOWELS))] # prints a random vowel
# print(x)

# # useful stuff
# Dir(var) # to get a list of methods you can preform on an object
# help(var.replace) # to get help on a method name
# ord('A') # convert from char to ascii
# chr(97) # convert from ascii to char
# # run startup stuff at interactive
# # in .bashrc  :  export PYTHONSTARTUP=$HOME/.pythonstartup
# # what version of python am I using?
# sys.version_info[:2]
# # current time
# now = time.strftime("%I:%M:%S %p", time.localtime())
# myIPaddress = socket.gethostbyname(socket.gethostname())
# print(sys.float_info.epsilon)

# # socket stuff http url web
# import socket, urllib.request
# destIP = socket.gethostbyname('166.161.24.101')
# destIP = socket.gethostbyname('google.com')
# response = urllib.request.urlopen("http://" + destIP)
# html = response.read()
# print(html)

# #string stuff
# b = isinstance("hi", str) # b == True
# s1 = 'sheep'
# s2 = 'dog'
# print("length of \"{}\" is {}".format(s1, len(s1)))
# print('{0}@{1}'.format('user', 'host')) # user@host
# n1 = 15.148
# print('{0}, {0:.2f}, {0:e}'.format(n1)) # 15.148, 15.15, 1.5148e+01
# print('{n1}, {n2}'.format(n1='hi', n2=5))
# s3 = 'Hi hello and hero'
# print(s3.lower().count('h')) # 3 ← there are 3 h's in s3
# print("print line with no new line at end", end="")
# mylist = ["a", "b", "c"]
# print("first = {0[0]}, second = {0[1]}".format(mylist)) 

# #Exception stuff
# import sys, os
# # to raise an exeption and catch it
# try:
	# raise NotImplementedError("No error")
# except Exception as e:
	# exc_type, exc_obj, exc_tb = sys.exc_info()
	# fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
	# print("Error: {}".format(exc_type))
	# print("\tIn file: {}".format(fname))
	# print("\tLine: {}".format(exc_tb.tb_lineno))
# # another example using lists, 
# # does one thing if catches IndexErrors
# # another for all other errors
# l = [1,2]
# try:
	# m = l[2]
# except IndexError as e:
	# exc_type, exc_obj, exc_tb = sys.exc_info()
	# fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
	# print("Error: {}".format(exc_type))
	# print("\tIn file: {}".format(fname))
	# print("\tLine: {}".format(exc_tb.tb_lineno))
# except Exception as e:
	# exc_type, exc_obj, exc_tb = sys.exc_info()
	# fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
	# print("Error: {}".format(exc_type))
	# print("\tIn file: {}".format(fname))
	# print("\tLine: {}".format(exc_tb.tb_lineno))

	
# #psutil stuff
# import psutil
# is named process running?
# ans = "cmd.exe" in [psutil.Process(i).name for i in psutil.get_pid_list()]
# print(ans)

# # Switch implementation
# def ff(x):
	# return x*x
# def gg(x):
	# return x**.5
# def hh(x):
	# return math.sin(x)
# var = "squareroot"
# value = int(input("enter a number: "))
# # switch case.  hh is default value
# ans = { "square":ff,
		# "squareroot":gg}.get(var, hh)(value)
# print(ans)

# # mutliple optional arguments in function calls
# def f(*args, **kwargs):
	# return 'args: {} kwargs: {}'.format(args, kwargs)
# print(f('a'))
# print(f(ar='a'))
# print(f(1,2, param=3))
