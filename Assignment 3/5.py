def Chkprime(ino):
	print("In check")
	print(ino)
	no=ino
	i=2
	for i in range(2,int((no/2)+1),1):
		if(no%i==0):
                        break
	if(i<int(no/2)):
                return False
	else:
                return True

def AcceptList():
	n=input("Enter n numbers")
	arr=list()
	
	for i in range(int(n)):
		no=int(input())
		arr.append(no)
	return arr

def do(arr):
	ans=0
	for i in range(len(arr)):
		value=Chkprime(arr[i])
		if(value==True):
			#print("In if")
			ans=ans+arr[i]
			#print("The ans is ",ans)		
	return ans
		
	
def main():
	arr=AcceptList()
	ans=do(arr)
	print("addtion is ",ans)
        #no,icnt=Count(arr)
        #rint("the {} occurs {} times".format(no,icnt))

if(__name__=="__main__"):
        main()

