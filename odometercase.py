
def odometer(n):
    a = str(n)
    count = 0
    for i in range(len(a) - 1):
    	if int(a[i]) >= int(a[i+1]):
            return 0
        else:
	    count += 1
    if count == len(a)-1:
  	return 1

def next(a):
    if a== read[0]:
    	return read[-1]
    return read[x+1]

def previous(a):
    if a== read[-1]:
    	return read[0]
    return read[x-1]

def next_n(a,n):
    if a== read[0]:
	return read[-n]
    return read[x+n]

def previous_n(a,n):
    if a== read[-1]:
	return read[n]
    return read[x-1-n]

a = int(input())
n = int(input())
read = [x for x in range(10 * len(str(a) - 1),10 * (len(str(a))]
print(read)
for i in read:
    if a == read[i]:
	print("next reading = ",next(i))
    	print("previous reading = ",previous(i))
        print("next reading  after ",n, " = ",next_n(i,n))
    	print("previous reading  after ",n, " = ",previous_n(i,n))






