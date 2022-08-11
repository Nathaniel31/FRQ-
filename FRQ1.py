
def mostCommonName(n):
	d = {}
	max_value = -1 
	mostName = "" 
	s = set()
	

	for name in n:
		if d.get(name,0) ==0:
			d[name]=1
		else: 
			d[name]+=1
	

