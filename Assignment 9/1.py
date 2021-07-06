import sys
import os

def ChkFile(file1):
	
	if(os.path.isfile(file1)):
		return True
	else:
		return False
	

def main():
	
	fobj=open(sys.argv[1],"r")
	
	if(ChkFile(sys.argv[1])==True):
		print("FIle exist")
	else:
		print("Not exist")
	
	fobj.close()			
		

if __name__=="__main__":
	main()
