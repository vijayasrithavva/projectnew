d = 'i'
count = 1
while d != '0':
	r = int(input())
	c = int(input())
	input_list =[]
	for i in range(r):
		x = input()
		input_list.append(x)
	print("Puzzle #",count)
	print("Across")
	for i in input_list:
		i = i.split('*')
		while '' in i:
			i.remove('')
		for j in i:
			print(' ',j)
	li1 = []
	print("Down")
	for i in range(c):
		b = ''
		for j in range(r):
			if input_list[j][i] == '*':
				break
			else:
				b += input_list[j][i]
		li1.append(b)

	for j in range(1,r):
		for i in range(c):
			p = ''
			if input_list[j][i] == '*':
				for k in range(j+1,r):
					if input_list[k][i] != '*':
						p += input_list[k][i]
					else:
						break
				li1.append(p)
			else:
				i += 1
	for i in li1:
		if i == '':
			continue
		else:
			print(' ',i)
	count += 1
	d = input()
	print()
