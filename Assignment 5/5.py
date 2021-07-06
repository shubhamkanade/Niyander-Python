ans=1
def FactR(no):
	if(no!=0):
		global ans
		ans=ans*no
		FactR(no-1)
	return ans


print(FactR(5))	
