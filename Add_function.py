def Add(no1 = 10,no2 = 10):
	ans=no1+no2;
	return ans;

x=input("enter first number : ");
y=input("enter second number : ");

ret=Add(x,y)  #Add() this is allowed becoz due to default argument
print("Addition is : ",ret)


#print Add(no1=12,no2=12);
