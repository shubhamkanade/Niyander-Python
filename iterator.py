class Topten:

	def __init__(self):
		self.num = 1
		
	
	def __iter__(self):
		return self


	def __next__(self):
		if(self.num <= 10):
			value = self.num
			self.num += 1
			return value
		else:
			raise StopIteration;
	
tp = Topten()

for i in tp:
	print(i)


	
