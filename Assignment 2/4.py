def SumFactor(num):
	sum=0
	for i in range(1,int((num/2))+1,1):
		if(num % i == 0):
			sum += i
	return sum

no=int(input("Enter a number"))
ret=SumFactor(no)
print(ret)	
