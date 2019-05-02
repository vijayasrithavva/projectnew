def isprime(n):
	if n == 2 or n == 3:
		return True
	
	for i in range(4,n//2):
		if n % i == 0:
			return False
	return True	

def factorize(n):
	factor = 2
	factors = []
	while n > 2:
		if n % factor == 0:
			if isprime(factor):
				factors.append(factor)
				n //= factor
		factor +=1
	return factors
print(max(factorize(600851475143)))		
