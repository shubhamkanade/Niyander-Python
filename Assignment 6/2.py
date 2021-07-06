class Circle:
	PI=3.14
	def __init__(self):
		self.radius=0.0
		self.area=0.0
		self.circumference=0.0

	def Accept(self):
		print( "Enter radius")
		self.radius=int(input())
		#area=int(input())
		#circumference=int(input())
	
	def Display(self):
		print("The radius,area,circumfernce is",self.radius,self.area,self.circumference)

	def CalculateArea(self):
		area=2*self.PI*self.radius*self.radius
		print(area)
	
	def CalculateCircumference(self):
		circumference=2*self.PI*self.radius
		print(circumference)
		
def main():
	obj1=Circle()
	obj2=Circle()
	obj1.Accept()
	obj1.Display()
	obj1.CalculateArea()
	obj1.CalculateCircumference()
	obj2.Accept()
	obj2.Display()
	obj2.CalculateArea()
	obj2.CalculateCircumference()


if __name__=="__main__":
	main()
	
