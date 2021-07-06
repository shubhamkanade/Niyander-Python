sum=0
def SumR(iNo):
	global sum
	if(iNo!=0):
		sum=sum+iNo%10
		SumR(iNo//10)
	
	return sum

res=SumR(879)
print(res)
