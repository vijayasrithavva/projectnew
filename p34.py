def factorize(n):
	a = 1
	while n > 1:
		a = a*(n-1)
	return a

sum = 0
for i in range(10,11):
	s = i
	a = 0	
	while i > 0:
		r = i % 10
		fact = factorize(r)
		a += fact
	if a == s:
		sum += s
print(sum)
	
