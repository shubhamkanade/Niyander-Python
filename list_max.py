def maximum(list):
	max = list[0]
	
	for value in list:
		if value > max:
			max = value
	return max


def main():
	
	list = [] 
	n = int(input("Enter N elements"))
	print("ENter elements")
	for i in range(n):
		list.append(int(input()))

	print("Maximum is ",maximum(list))

if __name__ == "__main__":
	main()

