def check(no):
	if no<0:
		no=-no
	icnt=0
	temp=no
	temp1=no
	while(no):
		icnt=icnt+1
		no/=10
	isum=0
	while temp:
		digit=temp%10
		ipow=1
		for i in range(0,icnt):
			ipow*=digit
		isum+=ipow
		temp/=10
	if isum==temp1:
		return True
	else:
		return False

x=input("Enter a number")

ret=check(x)

if(ret==True):
	print "armstrong number"
else:
	print "not armstrong number"

	
