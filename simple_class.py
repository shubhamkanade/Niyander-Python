print("Demonstartion of simple class")

class Demo:

	def __init__(self,value1,value2):
		self.i = value1
		self.j = value2

	def fun(self):
		print("in fun")
		print(self.i,self.j)

	def add(self):
		print(self.i + self.j)

	
dobj = Demo(10,20)

dobj.fun()

dobj1 = Demo(30,40)

dobj1.fun()

dobj.add()

dobj1.add()


