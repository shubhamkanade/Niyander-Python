def multiple(no):
	if no<0:
		no=-no
	if no==0:
		return
	for i in range(1,11):
		print no*i

x=input("ENter a number")
multiple(x)
