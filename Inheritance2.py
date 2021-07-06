class Demo:
	
	def __init__(self,value1,value2):
		self.no1=value1
		self.no2=value2

	def display(self):
		print "In Demo class"

class A:
	
	def __init__(self,no=10):
		self.value=no

	def display1(self):
		print "in a"
		
class Hello(Demo,A):
	
	def __init__(self,str='shubham'):
		self.str=str

	
hobj=Hello()
	
hobj.display()

hobj.display1()
