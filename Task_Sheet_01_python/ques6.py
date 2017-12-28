#Use recursive method to find factorial of a given number.
#Question 06

import sys

def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

arg1 = int(sys.argv[1])
print fact(arg1)

