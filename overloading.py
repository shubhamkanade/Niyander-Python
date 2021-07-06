class Vector:

	def __init__(self,a,b):
		self.a=a
		self.b=b

	def __add__(self,other):
		return self.a+other.a ,self.b+other.b

	def __str__(self):
		return "vector (%d %d)" % (self.a,self.b)		


v1=Vector(3,4)

v2=Vector(4,5)	

print v1+v2

print str(v1)


