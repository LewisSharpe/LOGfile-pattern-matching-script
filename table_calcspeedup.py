with open('log', 'r+') as f:
    for line in f:
        found = line.find('core-number-seq:') and line.find('core-number-1')
	print(found)        
	if found != -1:
           ## version = line[found+len('Server version:')+1:]
           ## print version