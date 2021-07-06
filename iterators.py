
class Demo:
	
	def __init__(self):
		self.no = 1

	def __iter__(self):
		return self

	def __next__(self):
		
		if self.no <= 10:
			val = self.no
			self.no += 1
			return val
		else:
			raise StopIteration

dobj = Demo()
print(next(dobj))	
print(next(dobj))

for i in dobj:
	print(i)
