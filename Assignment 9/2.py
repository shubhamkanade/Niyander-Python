import sys


def main():
	
	fobj=open(sys.argv[1],"r")
	
	print(fobj.read())
	
	fobj.close()	
	
if __name__=="__main__":
	
	main()
