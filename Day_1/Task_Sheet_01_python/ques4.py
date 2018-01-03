#Take two strings as input and find whether second string is present in first string.
#eg. python findPattern.py igdtuw gd
#Question 04

import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print arg2 in arg1
