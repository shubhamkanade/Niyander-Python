i=12

j=12
def fun():
	global i
	i=12
	print(id(i))


print(id(i))
print(id(j))
fun()
