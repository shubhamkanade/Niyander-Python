import sys

def main():

	if(len(sys.argv)<2):
		print("Enter valid arguments")
		exit()
	
	fobj=open(sys.argv[1],"r")

	ch=sys.argv[2]
	count=0
	arr=[]
	for a in fobj:
		arr=a.split(" ")
		print(arr,"   ",len(arr))		
		for i in range(len(arr)):
			if arr[i]==ch or arr[i]==ch+"\n":
				print(i)		
				count+=1
			
	
	print(ch+" word present {} times ".format(count))		

if __name__=="__main__":
	
	main()
