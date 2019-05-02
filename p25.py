f1 = f2 = 1
c = 3
f3 = f1 + f2

while f3 < 10**10:
	if len(str(f3)) == 1000:
		break
	else:
		f1, f2 = f2, f3
		f3 = f1 + f2
		c += 1
print(c)
