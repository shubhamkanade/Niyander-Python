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

def Displaylogfile(table):

	result=list(filter(lambda x:len(x)>1,table.values()))
	#print(result)
	if(len(result)>0):
		print("Duplicate found")
		for key in result:
			for value in key:
					fobj=open("Log.txt","a")
					fobj.write(value)					
def Directorywatcher(path):
	
	flag=os.path.isabs(path)
	 
	if flag==False:
		path=os.path.abspath(path)

	flag2=os.path.isdir(path)
	table={}
	if flag2:
		for folder,subfolders,files in os.walk(path):
			for fi in files:
				newpath=folder+"/"+fi
				checksum=hashfile(newpath)
				if(checksum in table):
					table[checksum].append(newpath)
				else:
					table[checksum]=[path]
	return(table)													          	
def main():
	
	arr=Directorywatcher(argv[1])
	Displaylogfile(arr)	
	
if __name__=="__main__":
	main()
