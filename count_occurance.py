a = [] 

n = int(input("Enter number of elements"))

for i in range(1,n+1):
	a.append(int(input("Enter element")))

cnt = 0

number = int(input("Enter number to be counted"))

for num in a:
	if(num == number):
		cnt += 1

print("count of %d number is %d"%(number,cnt))



