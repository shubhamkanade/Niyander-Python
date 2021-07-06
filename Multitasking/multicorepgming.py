from os import *
from multiprocessing import *

def square(no):
	print("In sqare pid is : ",getpid()) #here we are using only one core
	return (no*no)

def main():
	arr=[4,6,8,9,10,12]

	p1=Pool()
	brr=p1.map(square,arr)
	print(brr) #in this we are using four cores

if __name__=="__main__":
	main()
