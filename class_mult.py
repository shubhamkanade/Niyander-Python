
class Arithematic:

	def __init__(self,no1,no2):
		self.no1 = no1
		self.no2 = no2


	def mult(self):
		return self.no1 * self.no2


def main():
	
	no1 = int(input("Enter first number"))

	no2 = int(input("Enter second number"))
	
	obj = Arithematic(no1, no2)

	print("Multiplication is %d" % obj.mult())

if __name__ == "__main__":
	main()
