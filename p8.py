for i in range(1000):
	for j in range(i):
		for k in range(j):
			if i+j+k == 1000 and i**2 == j**2 + k**2:
				s = i*j*k
print(s) 
