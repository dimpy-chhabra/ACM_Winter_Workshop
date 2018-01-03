import ques8
import random
d = {}
d = ques8.read_file()

#print d
#print "\n"
with open('files_new.txt', mode='w') as outfile:	
	num = len(d.keys()) 
	for i in range(0,num):
		list = d[d.keys()[i]]
		#print list
		r = random.randint(0,1)
		if r==1:
			list[2] = str(random.randint(30,100))

		outfile.write(list[0]+' '+list[1]+' '+list[2]+'\n')
