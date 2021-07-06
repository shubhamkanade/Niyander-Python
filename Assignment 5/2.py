def Show(no):
	if(no!=0):
		Show(no=no-1)
		print(no,end=" ")

def main():
	value=int(input("ENter number"))
	Show(value)

if __name__=="__main__":
	main()
