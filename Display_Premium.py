def Display_Premium(age):
	if age<20:
		print "premium is 20000"
	elif age>=20 and age<45:
		print "premium is 35000"
	elif age>=45 and age<70:
		print "premium is 52000"
	else:
		print "premium is zero"

age=input("ENter a age :")

Display_Premium(age)


