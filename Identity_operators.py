a = 'john'
b='john'

if(a is b): # if a is same as b then returns true
 print("a is equal to b")
else:
 print("a is not equal to b")

if(id(a)==id(b)):
 print("a is equal to b")
else:
 print("a is not equal to b")
