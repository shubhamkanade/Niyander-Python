#i=0;
for num in range(10,20):
 for ie in range(2,(num/2)+1):  #range function is less than 
  if num%ie==0:
   break


 if ie>=(num/2):
  print num
  print "it is prime number"
 else:
  print num
  print "it is not prime number"
