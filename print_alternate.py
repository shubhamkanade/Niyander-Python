def print_alternate(list):
	print("in function")
	
	for no in range(0,len(list),2):
		print(list[no])		

def main():

        list_values = []
        n = int(input("Enter N Numbers"))

        print("Enter numbers")

        for i in range(n):
                list_values.append(int(input()))

        print_alternate(list_values)

main()
              
