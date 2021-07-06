def ChkPrime(num):
	for i in range(2,int(num/2)+1,1):
		if(num%i==0):
			break
	if(i<int(num/2)):
		return False
	else:
		return True

def main():
	num=int(input("Enter a number"))
	ret=ChkPrime(num)
	if(ret==True):
		print("It is prime")
	else:
		print("It is not prime")


if(__name__=="__main__"):
	main()
		
