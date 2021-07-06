#Lists are the most versatile of Python's compound data types. A list contains items
#separated by commas and enclosed within square brackets ([]). To some extent, lists
#are similar to arrays in C. One difference between them is that all the items belonging
#to a list can be of different data type.

#The values stored in a list can be accessed using the slice operator ([ ] and [:]) with
#indexes starting at 0 in the beginning of the list and working their way to end -1

list=["hello","john",0,3.14]	
tinylist=["shyam",123]
print list
print list[0]

print list[2:]

print list+tinylist # Prints concatenated lists

list[0]=4.0

print "after changing",list
