#in case of multiple which one we inherit first is gets called
class Base1:
	def fun(self):
		print("Base1 fun")
	
	def gun(self):
		print("Base1 gun")


class Base2:
	
	def fun(self):
		print("Base2 fun")

	
class Derived(Base2,Base1): #this is multilevel inheritance
	
	def run(self):
		print("Derived run")
		
	def sun(self):
		print("Derived sun")


def main():
	
	dobj=Derived()
	dobj.fun()
	dobj.sun()
 
if __name__=="__main__":
	main()
