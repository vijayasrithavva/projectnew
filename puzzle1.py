def input_data():
	li = [] 
	for i in range(5):
		x = list(input())
		li.append(x)
	y = input()
	return li,y

def find_position(a):
	x,y = 0,0
	for i in range(5):
		for j in range(5):	
			if a[i][j] == ' ':
				x,y = i,j
	return x,y

d = 'D'
count = 1
while d != 'Z':
	count1 = 1
	list1,y = input_data()
	i,j = find_position(list1)
	print("Puzzle #",count)
	for c in y:
		if i > 4 or j > 4 or i< 0 or j < 0:
			print('This Puzzzle has no final configuration')
			break
		else:
			if c == 'A':
				list1[i][j],list1[i-1][j] = list1[i-1][j],list1[i][j]
				i -= 1
			elif c == 'B':
				list1[i][j],list1[i+1][j] = list1[i+1][j],list1[i][j]
				i += 1
			elif c == 'R':
				list1[i][j],list1[i][j+1] = list1[i][j+1],list1[i][j]
				j += 1
			elif c == 'L':
				list1[i][j],list1[i][j-1] = list1[i][j-1],list1[i][j]
				j -= 1
			elif c == '0':
				break
			count1 += 1
	if count1 == len(y):
		for i in list1:
			for j in i:
				print(j,end= ' ')
			print()
	count += 1
	d = input()
			
