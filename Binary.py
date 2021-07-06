def Display(data):
	if '0'*6 in data or '1'*6 in data:
		print("has consecutive")
	else:
		print("not consecutive")


data=input()
Display(data)
