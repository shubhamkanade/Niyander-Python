def AcceptList():
	n = int(input("Enter n elements"))
	
	arr = list() #crerates empty list

	for i in range(0,n):
		arr.append(int(input())) #w/o int it takes in string
	
	return arr

def SumList(ret):
	#pass indicates empty defination
	sum=0
	for i in ret:
		sum=sum+i
	return sum 
			
def main():
	ret=AcceptList()
	ans=SumList(ret)
	print(ans)

if(__name__=="__main__"):
	main()

