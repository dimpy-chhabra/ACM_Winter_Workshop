#Take three numbers as input and find largest among them.
#eg. python findLarge.py 45 87 12  
#Question 03

import sys

s = 0
list = []
for arg in sys.argv[1:]:
	list.append(int(arg))
	#arg1 = sys.argv[1]

list.sort()
print list[len(list)-1]
