def Display(num):
	for i in range(num,0,-1):
		for j in range(i,0,-1):
			print("*",end='  ')
		print()
	

def main():
	no=int(input("Enter a number"))
	Display(no)
	

if(__name__=="__main__"):
	main()
