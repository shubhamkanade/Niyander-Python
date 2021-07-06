def calpower():

	i = 1
	
	while i <= 10:
		ans  = i * i
		yield ans
		i += 1

values = calpower()

#print(next(values))
#print(next(values))

for i in values:
	print(i)
