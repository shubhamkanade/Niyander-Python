from multiprocessing import *
import os

def fun(no):
	print("In fun")
	print("fun parent process",os.getppid())
	print("fun process",os.getpid())
	print('-'*40)

def run(no):
	print("in run")
	print("run parent process",os.getppid())
	print("run process",os.getpid())
	print('-'*40)

def gun():
	print("in gun")
	print("gun parent process",os.getppid())
	print("gun process pid",os.getppid())
	print("-" * 40)

def main():
	p1 = Process(target=fun,args = (3,))
	p1.start()
	
	p2 = Process(target = run,args = (6,))
	p2.start()
			
	p3 = Process(target = gun)
	p3.start()

	print("main pid ",os.getpid())
	print("main parent id ",os.getppid())

if __name__=="__main__":
	main()
