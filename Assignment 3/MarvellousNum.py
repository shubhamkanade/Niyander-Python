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

i=int(input("Enter number"))
ret=Chkprime(i)
if(ret==True):
	print("It is prime")
else:
	print("It is not prime")	
