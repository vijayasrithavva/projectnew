def summ(n):
	s = 2	

	for i in range(3,n,2):
		c = 0
		for j in range(2,i):	
			if i % j == 0:
				c += 1
		if c == 0:
			s += i
	return s
print(summ(20)) 
