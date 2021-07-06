def Display(no):
	if(no!=0):
		print(no,end=" ")
		Display(no-1)

def main():
	iNo=int(input("ENter value"))
	Display(iNo)

if __name__=="__main__":
	main()
	
