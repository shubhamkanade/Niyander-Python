def Bin(no):
	while(no):
		digit=int(no%2)
		print(digit,end=" ")
		no=int(no/2)

def BinR(no):
	if(no):
		digit=int(no%2)
		no=int(no/2)
		BinR(no)
		print(digit,end=' ')

no=int(input("Enter a number"))
Bin(no)
print()
BinR(no)
