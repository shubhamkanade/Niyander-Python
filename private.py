class Base:
		
	__num=0

	def printi(self):
		self.__num += 1
		print self.__num

bobj=Base()

bobj.printi()

#print bobj.__num //error
