from array import *

def Input():
	arr=array('d')

	num=int(input("Enter a number"))

	for i in range(0,num):
		arr.append(float(input()))

	print(arr)

def main():
	Input()

if __name__=="__main__":
	main()


