class Sparrow:
	
	def fun(cls):
		print("In fun method of sparrow")


class Aeroplane:
	
	def fun(cls):
		print("In fun method of aeroplane")

class Whale:

	def swim(cls):
		print("In swim method of whale")


def run(other):
		
	other.fun()

sobj = Sparrow()
aobj = Aeroplane()
wobj = Whale()

run(sobj)
run(aobj)
run(wobj)
