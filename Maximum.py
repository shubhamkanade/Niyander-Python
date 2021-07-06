def Maximum(no1,no2,no3):
	if (no1>no2 and no1>no3):
		return no1
	elif ((no2>no1 and no2>no3)):
		return no2
	else:
		return no3

fno1=input("Enter 1st number ")
fno2=input("Enter 2nd number ")
fno3=input("Enter 3rd number ")

result=Maximum(fno1,fno2,fno3)

print "maximum among 3 numbers is ",result
