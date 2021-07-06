def AcceptList():
        n=int(input("Enter n elements"))

        arr=list() #crerates empty list

        for i in range(0,n):
                arr.append(int(input())) #w/o int it takes in string

        return arr

def Count(arr):
	print("eNTER the number to search")
	no=int(input())
	icnt=0
	for i in arr:
		if(no==i):
			icnt=icnt+1
	return no,icnt
		
def main():
	arr=AcceptList()
	no,icnt=Count(arr)
	print("the {} occurs {} times".format(no,icnt))
	
if(__name__=="__main__"):
	main()
