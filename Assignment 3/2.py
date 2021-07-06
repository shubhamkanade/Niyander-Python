def AcceptList():
        n=int(input("Enter n elements"))

        arr=list() #crerates empty list

        for i in range(0,n):
                arr.append(int(input())) #w/o int it takes in string

        return arr


def ListMax(arr):
	max=arr[0]
	for i in arr:
		if(i>max):
			max=i
	return (max)

def main():
        ret=AcceptList()
        ans=int(ListMax(ret))
        print("The max is ",ans)

if(__name__=="__main__"):
        main()

