def AcceptList():
        n=int(input("Enter n elements"))

        arr=list() #crerates empty list

        for i in range(0,n):
                arr.append(int(input())) #w/o int it takes in string

        return arr


def ListMin(arr):
        min=arr[0]
        for i in arr:
                if(i<min):
                        min=i
        return (min)

def main():
        ret=AcceptList()
        ans=ListMin(ret)
        print("The min is ",ans)

if(__name__=="__main__"):
        main()

