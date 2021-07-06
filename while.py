def print_by_while(no):
	i = 1;
	while(i <= no):
		print(i)
		i = i + 1

def main():
	no = int(input("Enter number"))
	print_by_while(no)

if __name__ == "__main__":
	main()
