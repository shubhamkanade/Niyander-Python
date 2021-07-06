def Display_Factor(no):
	if no<0:
		no=-no
	
	for i in range(1,(no/2)+1):
		if no%i==0:
			print i

y=input("Enter number")

Display_Factor(y)
