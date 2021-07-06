def Display(num):
	for i in range(1,num+1,1):
		for j in range(1,num+1,1):
			print(j,end='  ')
		print()

def main():
	no=int(input("Enter a number"))
	Display(no)

if(__name__=="__main__"):
	main()

