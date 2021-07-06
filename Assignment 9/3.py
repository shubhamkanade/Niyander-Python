import sys

def main():
	
	fobj1=open(sys.argv[1],"a")
	fobj1.close()
	
	fobj1=open(sys.argv[1],"r")
	
	fobj2=open("Demo.txt","w")
	
	fobj2.write(fobj1.read())
		

if __name__=="__main__":
	
	main()
