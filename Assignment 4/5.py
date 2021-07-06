from functools import reduce

def AcceptData():
	n=int(input("Enter a number"))
	
	rlist=list()
	for i in range(0,n):
		num=int(input())
		rlist.append(num)
	return rlist

def Chkprime(ino):
	no=ino
	i=2	
	for i in range(2,int((no/2)+1),1):
		if(no%i==0):
			break
	#print(i)
	if(i<int(no/2)):
		return False
	else:
		return True

def Multiply(no):
	return no*2

def Max(no1,no2):
	if(no1>no2):
		return no1
	else:
		return no2	
def main():
	ans=AcceptData()
	print(ans)
	fdata=list(filter(Chkprime,ans))
	print(fdata)
	mdata=list(map(Multiply,fdata))
	print(mdata)
	rdata=reduce(Max,mdata)
	print(rdata)	

if(__name__=="__main__"):
	main()
