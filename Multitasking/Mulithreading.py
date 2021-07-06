from multiprocessing import *
from os import *
from threading import *

def fun(ino):
	for i in range(5):
		print(i)
	print("Hello ",ino ,"from fun")
	print("in fun pid is :",getpid())
	print("In fun ppid is :",getppid())

def gun(ino):
	for i in range(5):
		print(i)
	print("Hello ",ino,"from gun")
	print("In gun pid is :",getpid())
	print("In gun ppid is :",getppid())

def main():
	p1=Thread(target=fun,args=(20,))
	p2=Thread(target=gun,args=(20,))
	print("In main pid is",getpid())
	print("In main ppid is ",getppid())
		
	p1.start() #it is another process main is parent becoz it is calling
	p2.start() #it is another process main is parent becoz it is calling
	

if __name__=="__main__":
	main()
