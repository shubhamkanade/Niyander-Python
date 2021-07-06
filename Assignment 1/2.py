def ChkNum(iNo):
	if(iNo%2 == 0):
		return True
	else:
		return False


num=input("Enter a number")
#num=input()

ret=ChkNum(int(num))

if(ret==True):
	print("Even number")
else:
	print("Odd number")


