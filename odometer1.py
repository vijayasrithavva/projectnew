def validity(read1):
	read = str(read1)
	if read1 % 10 == 0 or read1 < 12 or int(read[1]) <= int(read[0]) or read1 > 89:
		return False
	return True
read1 = int(input("reading : "))
read = str(read1) 

if read1 %10 == 0 or read1 < 12 or int(read[1]) <= int(read[0]) or read1 >89:
	print("invalid input")

else:
	if(validity(read1 - 1) == True):
		print("previous reading",read1 - 1)
	else:
		r = (int(read[0])-1)*10 + 9
		if r <= 9:
			print("previous reading = 89")
		else:
			print('previous reading',r)
	if validity(read1 + 1) == True:
		print("Next reading = ",read1 + 1)
	else:
		w = (int(read[0])+1)*10 + (int(read[0])+2)
		if w >= 90:
			print("Next reading = 12")
		else:
			print("Next reading =",w)
