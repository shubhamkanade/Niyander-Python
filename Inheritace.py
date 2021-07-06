class Demo:

	def fun(self):
		print("Inside fun")

	def gun(self):
		print("Inside gun")
		
	@classmethod
	def run(cls):
		print("Inside run")

	@staticmethod
	def mun():
		print("Inside static method")

class Remo:

	def fun(self):
		print("Inside fun of Remo")
	

class Hello(Remo,Demo):
	
	def run(self):
		print("Inside run")

def main():

	hobj = Hello()
	hobj.fun()
	
	dobj = Demo()
	dobj.run()
	dobj.mun()
	dobj.gun()

main()
