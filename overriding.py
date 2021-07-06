class base:
	
	def mymethod(self):
		print "in base class"
	

class derived(base):

	def mymethod(self):
		print "in derived class"

b=base()

b=derived()

b.mymethod()
