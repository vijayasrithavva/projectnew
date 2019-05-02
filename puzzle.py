li = []
for i in range(1,6):
	
		x = input()
		li.append(x)			
x1 = []
a = input()
x1.append(a)	
for k in range(len(x1)):
	x = x1[k]
	for i in range(1,6):
		for j in range(1,6):
		
			if li[i][j] == ' ':
				a = li[i][j]
	
			if x =='A':
				a,li[i-1][j] = li[i-1][j],a
			elif x =='B':
				a,li[i+1][j] = li[i+1][j],a
			elif x == 'R':
				a,li[i][j+1] = li[i][j+1],a
			elif x == 'L':
				a,li[i][j-1] = li[i][j-1],a
			else:
				
