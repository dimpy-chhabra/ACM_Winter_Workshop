#Use iterative method to find factorial of a given input number.
#Question 05

import sys

arg1 = int(sys.argv[1])
i = 1
fact = 1
for i in range(1, arg1+1):
	fact = i*fact

print fact
