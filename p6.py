
def sum(n):
	s = 0
	for i in range(n+1):
		s += i**2
	return s

def square(n):
	r = 0
	for i in range(n+1):
		r += i
	return r * r
print(square(100) - sum(100))
