class Numbers:
	
	def __init__(self,ino):
		self.ino=ino

	def Chkprime(self):
		#print("In check")
		#print(ino)
		no=self.ino
		i=2
		for i in range(2,int((no/2)+1),1):
			if(no%i==0):
                        	break
		if(i<int(no/2)):
                	return False
		else:
                	return True

	def Chkperfect(self):
		
		if(self.SumFactors()==self.ino):
			return True
		else:
			return False

	def Factors(self):
		for i in range(1,int(self.ino/2)+1,1):
			if(self.ino%i==0):
				print(i)

	def SumFactors(self):
		sum=0
		for i in range(1,int(self.ino/2)+1,1):
			if(self.ino%i==0):
				sum+=i	
		return sum

def main():					
	nobj=Numbers(5)
	if(nobj.Chkprime()==True):
		print("It is prime")
	else:
		print("it is not prime")

	nobj2=Numbers(6)
	if(nobj2.Chkperfect()==True):
		print("It is perfect")
	else:
		print("It is not perfect")
	
	nobj2.Factors()
	print(nobj2.SumFactors())

if __name__=="__main__":
	main()
