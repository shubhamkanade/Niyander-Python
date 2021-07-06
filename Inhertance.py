class Base:
	def __init__(self,np=10):
		print "Inside constructor"
		self.no=np

	def baseM(self):
		print "inside base method"

class derived(Base):
	def __init__(self):
		print "Inside derived constructor"
		
	
	def derivedM(self):
		print "inside derived method"


cobj=derived()

bobj=Base()
cobj.baseM()
cobj.derivedM()

print cobj.no
