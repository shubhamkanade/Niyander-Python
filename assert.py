#The assert Statement
#When it encounters an assert statement, Python evaluates the accompanying
#expression, which is hopefully true. If the expression is false, Python raises
#an AssertionError exception.

def fun(number):
	assert number>0,"number cannot be negative"

	return number+1;

print(fun(5))

print(fun(3))

print(fun(-1))

