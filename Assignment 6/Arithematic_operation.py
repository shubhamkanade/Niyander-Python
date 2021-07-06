class Arithematic:
	
	def __init__(self,no1,no2):
		self.value1 = no1
		self.value2 = no2

	def add(self):
		return self.value1 + self.value2
	
	def sub(self):
		return self.value1 - self.value2


def main():
	
	no1 = int(input("Enter first number"))	
	no2 = int(input("Enter second number"))
	
	aobj = Arithematic(no1,no2)

	print("Addition is ",aobj.add())

	print("Subtraction is ",aobj.sub())

main()

