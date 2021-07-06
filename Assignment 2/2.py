def Display(num):
	for i in range(1,num+1,1):
		for j in range(1,num+1,1):
			print("*",end='  ')
		print()


num=input("Enter a number")

Display(int(num))
		
