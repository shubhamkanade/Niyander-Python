def fun():
	print("In fun")
	def gun():
		print("In gun")
	gun()

def main():
	fun()

if __name__ == "__main__":
	main()
