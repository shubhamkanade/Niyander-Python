#In python two types of variable class and instance variable
#in pythoin there are three types of methods class,static,instance
#if we want to create instace variable(object variable) then we have to create inside init method
#__init__() is just like constructor that we use another language

class Demo:
	
	data=5.49 # it is class variable accessed by class as well as object 
	
	def __init__(self,value1,value2):
		self.no1=value1      #instance variable(no1)
		self.no2=value2	#instance variable(no2)
		
	@classmethod #decorators 
	def mun(cls) :#class method  for which cls parameter is compulsory accr to standards
		print("Hello mun")
		#print(cls.no1) not allowed
		print(cls.data)
	
	def fun(self):  #instance method for 
		print("Inside Demo fun")
		print(self.no1)
	
	def gun(self):  #instance method ,self is compulsory parametr indicates just like a this pointer in c++
		print("Inside Demo gun")

	@staticmethod
	def smethod():
		print("Inside static method")

def main():
	dobj=Demo(3,4)  
	dobj.fun() #fun(dobj) =>fun(0x100) standard way of caling this is below 
	dobj.gun() #gun(dobj) =>fun(0x200)
 
	#Demo.fun(dobj) #another way of calling indirect way

	Demo.mun()
	dobj.mun() #class method can be called by using object name as well as class name
	
	Demo.smethod() 
	dobj.smethod()
	print(dobj.data)

if __name__=="__main__":
	main()
