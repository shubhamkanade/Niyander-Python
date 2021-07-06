class BankAccount:
	ROI = 10.5

	def __init__(self,name,amount):
		self.name=name
		self.amount=amount

	def Deposit(self,value):
		self.amount=self.amount+value
		#print(amount)
	

	def Withdraw(self,value):
		self.amount=self.amount-value
		
	def CalculateInterest(self):
		print(ROI)

	def Display(self):
		print(self.name,self.amount)
	
	
def main():
	bobj1=BankAccount("shubham",3400)
	bobj2=BankAccount("sachin",4359)
	
	bobj1.Deposit(1000)
	bobj1.Display()
	
	bobj2=BankAccount("swapnil",2390)
	
	bobj2.Deposit(500)
	bobj2.Display()
	bobj2.Withdraw(200)
	bobj2.Display()
	

main()
