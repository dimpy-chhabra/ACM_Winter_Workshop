#Take a bunch of strings as input and output them in alphabetical order.
#eg. python strSorter.py igit igdtuw india
#Question 02

import sys

s = 0
list = []
for arg in sys.argv[1:]:
	list.append(arg)
	#arg1 = sys.argv[1]

list.sort()
for arg in list:
	print arg

