def Factorial(num):
	fact=1
	while(num!=0):
		fact=fact*num
		num=num-1
	return fact

no=int(input("Enter a number"))
ret=Factorial(no)

print(ret)
	
