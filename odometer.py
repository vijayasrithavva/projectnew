a = []
for i in range(12,90):
	c = i
	if i%10 >= i//10:
		continue
	else:
		a.append(c)
b = input()
for i in a:
	if b == a[i]:
		if b == 12:
			print('previous reading = 89\n next reading =',a[i+1])
		elif b == 89:
			print('previous reading =',a[i-1],'\nnext reading = 12')
		else:
			print('previous reading =',a[i-1],'\nnext reading =',a[i+1])
	else:
		print('invalid input')			 	
	


