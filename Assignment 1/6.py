def Display(num):
	if(num>0):
		print("Positive number")
	elif(num<0):
		print("Negative number")
	elif(num==0):
		print("Zero")


no=input("Enter a number")

Display(int(no))
