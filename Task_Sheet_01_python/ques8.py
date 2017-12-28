def read_file():
	d = {}
	with open("file.txt") as f:
		for line in f:
			list = []
			list_ = []
			list = line.split(',')
			list_ = list[2].split('\n')		
			list[2] = list_[0]
			#print list
			(key, val) = (list[1], list)
			d[(key)] = val
	#print d
	return d
#read_file()
