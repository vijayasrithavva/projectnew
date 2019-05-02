def revs(num):
	num = str(num)
	if num[::-1] == num:
		return True
	return False
list = []
for i in range(100,1000):
	for j in range(100,1000):
		if revs(i * j):
			list.append(i*j)
print(max(list))			

