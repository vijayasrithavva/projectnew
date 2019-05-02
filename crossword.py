r = int(input("no of rows:"))
c = int(input("no of columns:"))

names = []
for i in range(r):
	x = input()
	names.append(x)

print("Across")	
for i in names:
	i = i.split('*')

	while '' in i:
		i.remove('')
	for j in i:
		print(j)

print("Down")
list1 = []
for i in range(c):
	x =''
	for j in range(r):
		x += list1[j][i]
		list1.append(x)
for i in list1:
	i = i.split('*')
	while '' in i:
		
