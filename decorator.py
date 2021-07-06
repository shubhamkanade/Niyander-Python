def sub(no1,no2):
	return no1 - no2

def Decorator(orignalfun):
	def updator(a,b):
		if(a < b):
			a,b = b,a
		return orignalfun(a,b)
	return updator

newSub = Decorator(sub)

print(newSub(6,7))
