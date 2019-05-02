a = 100
s = a
sum = 0
while a > 1:
	s *= (a-1)
	a -= 1
while s > 0:
	r = s % 10
	sum += r
	s //= 10
print(sum)	


