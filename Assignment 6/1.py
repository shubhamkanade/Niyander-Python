class Demo:

	Value=20
	
	def __init__(self,value1,value2):
		self.no1=value1
		self.no2=value2
	
	def fun(self):
		print("value is {}".format(self.no1))
		print("Value is {}".format(self.no2))

	def gun(self):
                print("value is {}".format(self.no1))
                print("Value is {}".format(self.no2))

def main():
	obj1=Demo(11,21)
	
	obj2=Demo(52,101)
	
	obj1.fun()
	obj2.fun()
	obj1.gun()
	obj2.gun()

if __name__=="__main__":
	main()
