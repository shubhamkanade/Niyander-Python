icnt=1
def Pattern(i,j):
	for i in range(1,i+1,1):
		global icnt
		icnt=1
		for j in range(1,j+1,1):
			if(j%2==0):
				print("#",end=" ")
			else:
				print(icnt,end=" ")
				icnt+=1
		print()

Pattern(3,5)
