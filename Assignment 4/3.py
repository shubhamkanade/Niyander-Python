from functools import reduce
def AcceptData():
	num=int(input("Enter N number"))
	
	arr=list() #make an empty list
	for i in range(0,num):
		value=int(input())
		arr.append(value)
	return arr

def filterdata(no):
	if(no>=70 and no<=90):
		return no

def Increse(ino):
	return ino+10	

def Prod(no1,no2):
	return no1*no2

def main():
	ans=AcceptData()
	filterd=list(filter(filterdata,ans))
	print("Filtered data",filterd)
	mapdata=list(map(Increse,filterd))
	print("Map data",mapdata)
	reducedata=reduce(Prod,mapdata)
	print(reducedata)

if(__name__=="__main__"):
	main()	
