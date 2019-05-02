a = 2**1000
s = 0
while a > 0:
	r = a % 10
	s += r
	a //= 10	
print(s)
