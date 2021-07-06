class A:
	
	def __init__(self,no1):
		self.no1 = no1	
	def fun(self):
		print("In a")

class B:
	
	def fun(self):
		print("In B")

class C(A,B):
	
	def gun(self):
		print("In C")

def main():	
	cobj = C(3)

	cobj.fun()
	
if __name__ == "__main__":
	main()
