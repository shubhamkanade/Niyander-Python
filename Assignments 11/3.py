import os
from sys import *
import hashlib

def deletefile(arr):
		
	brr=list(filter(lambda x :len(x) >1,arr.values()))
	icnt=0
	if len(brr)>0:
		print("Dupliate File found")
		for fil in brr:
			for name in fil:
				icnt+=1
				if(icnt>=2):
					os.remove(name)
			icnt=0
	else:
		print("No duplicate file found")	
				
		
def hashfile(path,blocksize=1024):
	
	fd=open(path,'rb')
	hasher=hashlib.md5()
	buf=fd.read(blocksize)
	
	while(len(buf)>0):
		hasher.update(buf)
		buf=fd.read(blocksize)

	fd.close()
	return hasher.hexdigest()

def PrintDuplicate(table):
	
	results=list(filter(lambda x:len(x)>1,table.values()))
	if(len(results)>0):
		for result in results:
			for sub in result:
				fobj=open("x.txt","a")
				fobj.write(sub)
		print("Outside for") 	
		
def createhash(path):
	#print("In createhash")
	flag=os.path.isabs(path)
	
	if flag==False:
		path=os.path.abspath(path)
		#print(path)
	
	flag2=os.path.isdir(path)
	#print(flag2)
	dups = {}
	if flag2 ==True:
		for folder,subfolder,files in os.walk(path):
			print("folder name"+folder)			
			for fi in files:
				newpath=os.path.join(folder,fi)
				file_hash=hashfile(newpath)
		
				if file_hash in dups:
					dups[file_hash].append(newpath)
				else:
					dups[file_hash]=[newpath]
		return dups		
def main():

	print("--------Developed by shubham kanade----------")
	print("This is used to remove all duplicate files")
	if(len(argv)!=2):
		print("Enter valid Arguments check command parameters")
		exit()
	#lobj=Lock()	
	arr = {}
	arr=createhash(argv[1])
	#print(arr)
	#lobj.acqiure()		
	PrintDuplicate(arr)
	#lobj.release()
	deletefile(arr)			
	
	#except(Exception):
	#print(Exception)
	
	print("Thanks for using our script")	

if __name__=="__main__":
	main()	
