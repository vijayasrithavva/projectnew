a = list( x for x in range(12,90) if x % 10 > x // 10 and x % 10 != 0 and x // 10 != 0)
b = input()

if b == a[0]:
	print("previous reading ="a[-1])
	


