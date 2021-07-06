class Base:
	def __init__(self,no1,no2):
		self.no1=no1
		self.no2=no2
	
	def __eq__(self,oth):
		return self.no1	== oth.no1 and self.no2 == oth.no2
		
	def Sub(self):
		return self.no1-self.no2	
		
	def Mult(self):
		return self.no1*self.no2

bobj1=Base(3,4)

bobj2=Base(3,4)

print bobj1.Sub()

print bobj1.Mult()

print bobj1==bobj2  #like opearator overloading
