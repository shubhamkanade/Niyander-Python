def CountDigit(num):
	icnt = 0
	while(num != 0):
		icnt = icnt + 1
		num=num // 10
	return icnt

def main():
	iNo1=int(input("Enter a number"))
	result=CountDigit(iNo1)
	print("digits are ",result)

if(__name__=="__main__"):
	main()


