import os
from sys import *
import hashlib

def hashfile(path,blocksize=1024):
	
	fd=open(path,'rb')
	hasher=hashlib.md5()
	buf=fd.read(blocksize)
	
	while(len(buf)>0):
		hasher.update(buf)
		buf=fd.read(blocksize)

	fd.close()
	return hasher.hexdigest()

def Directorywatcher(path):
	
	flag=os.path.isabs(path)
	
	if flag==False:
		path=os.path.abspath(path)

	flag2=os.path.isdir(path)
	
	print("-"*100)	
	if flag2:
		for folder,subfolders,files in os.walk(path):
			for fi in files:
				newpath=folder+"/"+fi
				print(newpath + "   "+hashfile(newpath))
	else:
		print("Enter correct directory name")							
def main():
	print("----------Developed by shubham kanade-----------")
	print("welcome to this script ")
	print("for using this script use any of the below commands")
	print("for help use => python3 filename -h ")
	print("For usage use =>python3 filename -u")
	print("for running use =>python3 filename directory_name")
	if(len(argv)!=2):
		print("Invalid arguments")
		print("Enter from above information")
		exit()
	try:	
		Directorywatcher(argv[1])

	except Excpetion as e:
		print(e)
if __name__=="__main__":
	main()
