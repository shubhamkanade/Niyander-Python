from sys import *

def main():
	
	if(len(argv)<3):
		print("Enter valid arguments")
		exit()
	
	fobj1=open(argv[1],"r")
	fobj2=open(argv[2],"r")

	if(fobj1.read()==fobj2.read()):
		print("Files data are same")
	else:
		
		print("Files data are not same")

if __name__=="__main__":
	
	main()
