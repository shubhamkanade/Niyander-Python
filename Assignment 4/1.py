def Calpow(iNo):
	return iNo*iNo

def main():
	iNo=int(input("Enter number"))
	ans=Calpow(iNo)
	print("The power of {} is {} ".format(iNo,ans))
	
if(__name__=="__main__"):
	main()
