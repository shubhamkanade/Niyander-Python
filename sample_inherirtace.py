class A:
	
	def __init__(self,*args):	
		self.list1 = args
	
	def show(self):
		print(self.list1)

aobj = A(3,4)

aob1 = A(5)

aobj2 = A(2,3,4,5,7,8)

aobj.show()
