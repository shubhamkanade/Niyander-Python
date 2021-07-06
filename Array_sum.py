def Add(arr):
	sum=0
	i=0
	for x in arr: # x itself contain number
		sum=sum+x;
	return sum;

arr=[3,7,9,4]

n=len(arr)

sum=Add(arr)

print sum
