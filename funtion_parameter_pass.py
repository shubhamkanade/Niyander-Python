#All parameters (arguments) in the Python language are passed by reference. It
#means if you change what a parameter refers to within a function, the change also
#reflects back in the calling function


def change(lis):
	print "In a function"
	lis.append([1,2,3,4])
	return



List=[10,20,30,40]

change(List)

print "after calling function ",List
