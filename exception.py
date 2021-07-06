
try:
	fo=open("fun.txt","wb+")
	fo.write("hello hi");
except IOError:
	print "file is missing"
else:
	print "written successfully"

