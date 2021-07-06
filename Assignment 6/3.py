class Arithematic:

	def __init__(self):
		self.no1=0
		self.no2=0
	
	def Accept(self):
		self.no1=int(input("Enter 1st number"))
		self.no2=int(input("Enter 2nd number"))

	def Add(self):
		return self.no1+self.no2
	
	def Sub(self):
		return self.no1-self.no2
	
	def Mult(self):
		return self.no1*self.no2

	def Div(self):
		return self.no1/self.no2
	
	
def main():
	aobj1=Arithematic()
	aobj2=Arithematic()
	
	print(aobj1.Accept())
	print(aobj1.Add())
	print(aobj1.Sub())
	print(aobj1.Mult())
	print(aobj1.Div())

if __name__=="__main__":
	main()
