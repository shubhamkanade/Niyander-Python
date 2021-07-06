from os import *
from multiprocessing import *

def mult(no):
	print("in mult pid ",getpid())
	return (no * 2)

def main():
	
	arr = [2,3,4,5,6,7,8]

	p1 = Pool()
	brr = p1.map(mult,arr)

	print(brr)

if __name__ == "__main__":
	main()
