class Bookstore:
	No_of_books = 0
	def __init__(self,name,author):
		self.name = name
		self.author = author
		Bookstore.No_of_books += 1
	
	def Display(self):
		print(self.name,self.author,self.No_of_books)			

def main():
	bobj = Bookstore("Linux System programming","Robert love")
	bobj.Display()

	bobj1 = Bookstore("C programming","Dennis Ritchie")
	bobj1.Display()

main()
	
