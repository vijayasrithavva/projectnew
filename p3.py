n = 600851475143
c = 0
max = 0
for i in range(1, n):
	for a in range(2,i):
		if i % a == 0:
			c += 1
	if n % i == 0 and c == 0:
		max = i
print(max)
