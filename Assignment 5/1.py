def Pattern(iNo):
	if(iNo != 0):
		print("*",end = " ")
		Pattern(iNo = iNo - 1)

def main():
	no = int(input("Enter number"))
	Pattern(no)

if __name__=="__main__":
	main()
