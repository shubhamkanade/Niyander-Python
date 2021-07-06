class Sample:
	def __init__(self,a,b):
		self.no1=a
		self.no2=b

	def Mul(self):
		return self.no1*self.no2
	

	
sobj=Sample(3,5)

ans=sobj.Mul()

print ans
