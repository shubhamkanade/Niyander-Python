def main():
	no=int(input("Enter N elements"))
	arr=list() #make a empty list

	print("Enter elements")
	for i in range(no):
		num=int(input())
		arr.append(num)

	print(arr)

if(__name__=="__main__"):
	main()
