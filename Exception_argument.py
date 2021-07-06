# Define a function here.
def temp_convert(var):
	try:
		return int(var)
	except ValueError, Arg:
		print "The argument does not contain numbers\n", Arg
# Call above function here.
temp_convert("xyz");
