#An object's attributes may or may not be visible outside the class definition. You need
#to name attributes with a double underscore prefix, and those attributes then are not
#be directly visible to outsiders.

class Base:
	__no=0

	def count(self):
		self.__no += 1 
		print self.__no

b=Base()
b.count()
#print b.__no  # error

print b._Base__no # 1 
