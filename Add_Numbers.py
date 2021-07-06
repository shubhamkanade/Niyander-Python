def add_number(no):
	
	sum = 0;
	for i in range(1,no+1):
		sum = sum+i
	return sum

x = int(input("Enter a number"))
ret = add_number(x)

print("the sum is ",ret)
