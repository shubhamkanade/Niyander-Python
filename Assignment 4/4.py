from functools import reduce

def AcceptData():
	n = int(input("Enter N number"))
	
	brr = list()
	for i in range(0,n):
		num = int(input())
		brr.append(num)
	return brr

def even(no):
	return not no%2

def cals(no):
	return no*no

def add(no1,no2):
	return no1 + no2
	
def main():
	ans = AcceptData()
	print(ans)
	fdata = list(filter(even,ans))
	print(fdata)
	mdata = list(map(cals,fdata))
	print(mdata)
	rdata = reduce(add,mdata)
	print(rdata)

if(__name__=="__main__"):
	main()
