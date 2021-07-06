def SumDigits(num):
	sum = 0
	while(num != 0):
		sum = sum + num%10
		num=num // 10
	return sum


def main():
	iNo1 = int(input("Enter a number"))
	ret=SumDigits(iNo1)
	print(ret)

if(__name__=="__main__"):
	main()
