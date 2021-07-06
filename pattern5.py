rows = int(input("Enter rows"))

for i in range(1,rows+1,1):
	for j in range(1,(rows * 2-1)+1,1):
		if( (j <= (rows+1)-i) or (j >= (rows-1)+i)):
			print("*",end=" ")
		else:
			print(end="  ")

	print()

