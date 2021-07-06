def Display_fees(std):
	if std==4:
		iFess=20000
	elif std==5:
		iFess=15000
	elif std==6 or std==7:
		iFess=22000
	elif std==8:
		iFess=32000
	elif std==9 or std==10:
		iFess=31000
	else:
		iFess=0
	return iFess

x=input("Enter standard")

ret=Display_fees(x)

print "The fees for ",x,"statndard is ",ret


