from threading import *
from os import *

def fun(no):
	print("In fun method")
	print("fun parent process",getppid())
	print("fun thread's process pid ",getpid())
	print("-"*50)


def run(no):
	print("in run method")
	print("run parent process",getppid())
	print("fun thread's process pid",getpid())

def main():
	t1 = Thread(target = fun,args = (4,))
	t2= Thread(target = run,args = (5,))
	
	print("main process pid",getpid())
	print("main parent process pid",getppid())
	print("-"*50)
	t1.start()
	t2.start()

if __name__ =="__main__":
	main() 
