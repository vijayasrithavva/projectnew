sum = 0
for i in range(2,10000000):
	s = i
	a = 0
	while i > 0:
		r = i % 10
		a += r**5
		i //= 10
	if s == a:	
		sum += a
print(sum) 
