"""
#1
for i in "hello":
	print(i)

#2
for letter in "Python":
	print('Current letter',letter)
fruits = ['banana','apple','mango']
for fruit in fruits:
	print('Current fruit',fruit)
"""




#Loop Control Statements

'''1.break :-  break statement is a jump statement which is used to transfer execution control.
		 and in case of inner loop,inner loop terminates immediately and resumes execution 			 at the next statement. The break statement can be used in both for and while 			 loops. 	
2.continue :-  It returns the control to the beginning of the loop. the continue statement 		 rejects all the remaining statements in the current iteration and moves the 		 control back to the top of the loop. The continue statement can be used in    			 both for and while loops. 
3.pass	    :-	 It is used when a statement is required syntactically but you do not want any 			 command or code to execute. The pass statement is null operation;nothing happens 			 when it executes.
'''

#1.break


for letter in "saurabh":
	if letter == 'b':
		break
	print("Current Letter:",letter)



#2.continue

for letter in 'shubham':
	if letter == 'b':
		print("In continue")
		continue
	print('Current Letter:',letter)


#3.pass

for letter in 'akshay':
	if letter == 's':
		pass
		print("Pass Block")
	print("Current letter:",letter)
