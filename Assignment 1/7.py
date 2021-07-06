def ChkDiv(num):
	if(num%5 == 0):
		return True
	else:
		return False
	

x=int(input("Enter a number"))
ret=ChkDiv(x)

if(ret==True):
	print("it is divisible by 5")
else:
	print("It is not divisible by 5")



