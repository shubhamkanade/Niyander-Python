def min(list):
	
	min = list[0]
	max = list[0]
	
	for no in list:
		if no < min:
			min = no
		elif no > max:
			max = no

	return max - min

def main():

	list_values = []
	n = int(input("Enter N Numbers"))

	print("Enter numbers")
	
	for i in range(n):
		list_values.append(int(input()))

	print("Difference between max and min is ",min(list_values))

main()
