total=0  # this is a global variable

def multiply(a,b):
	total=a*b   # this is a local variable
	return total


def main():
	print(multiply(4,5))

main()
