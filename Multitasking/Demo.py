import sys
from sys import *
from os import *

from multiprocessing import *

def fun():
	print("The pid is ",getpid())

def main():
	print("The entry point function pid is ",getpid()) #for main terminal is parent process
	fun()

if __name__=="__main__":
	main()
