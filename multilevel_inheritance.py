class A:
	
	def __init__(self,value1):
		self.no1=value

	def print1(self):
		print "in A class"

class B(A):
	
	def __init__(self,str="shubhu"):
		self.s=str
		
	def print2(self):
		print "in B class"

class C(B):
		
	def __init__(self,no1=55.07):
		self.fvalue=55.07

	def print3(self):
		print "In c class"


cobj=C()
cobj.print1()
cobj.print2()
cobj.print3()		

cobj.fvalue		
