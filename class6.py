class Arithematic:

	def __init__(self, value1, value2):
		self.no1 = value1
		self.no2 = value2

	def Add(self):
		return self.no1 + self.no2

	def Sub(self):
		return self.no1 - self.no2

def main():
	
	no1 = int(input("Enter 1st number\n"))
	no2 = int(input("ENter 2nd number\n"))

	aobj = Arithematic(no1,no2)
	
	print("Addition is",aobj.Add())
	print("Subtraction is",aobj.Sub())
	
main()
