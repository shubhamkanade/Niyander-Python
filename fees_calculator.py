def fees_cal(std):
	
	fees = 0
		
	if(std <= 0):
		return -1
	
	if(std == 4):
		fees = 25000
	elif(std == 5):
		fees = 30000
	elif(std == 6):
		fess = 35000
	else:
		print("Not a valid standard");
		exit(0)
	return fees
def main():
	
	std = int(input("Enter standard"))
	
	print(fees_cal(std))

if __name__ == "__main__":
	main()
