class Hello:

	def Display1(self):
		print "In super class"
	
class Demo(Hello):
	
	def __init__(self,a):
		self.no1=a

	def Display(self):
		print "In sub class"


dobj=Demo(3)

print dobj.Display1()
