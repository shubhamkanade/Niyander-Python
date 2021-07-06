try:
	fh = open("testfile", "w")
	#fh.read(2)
	try:
		fh.write("hehhe")
	finally:
		print "Going to close the file"
		fh.close()
except IOError:
	print "Error: can\'t find file or read data"
