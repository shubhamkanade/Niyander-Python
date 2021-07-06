def Sub(no1,no2):
	ret  = 0
	if no1 != 0 and no2 != 0:
		ret = no1 - no2
		return ret

def main():
	no1 = int(input("ENter First number"))
	no2 = int(input("Enter second number"))
	print(Sub(no1,no2))

if __name__ == "__main__":
	main()
