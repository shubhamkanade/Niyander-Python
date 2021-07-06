
def doc(fun):

	def run():
		print("Before")
		
		fun()
		print("After run")
	return run

@doc
def sub():
	print("In sub")

'''@sub
def mun():
	print("In run")
'''
#res = doc(sub)

sub()

#mun()
