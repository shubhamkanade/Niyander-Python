class Hello:
	
	def __init__(self,no1,no2):
		self.value1 = no1
		self.value2 = no2

	def add(self):
		return self.value1 + self.value2

def main():
	no1 = int(input("Enter first number"))
	no2 = int(input("Enter second number"))
	
	hobj = Hello(no1,no2)
	print(hobj.add())

main()

