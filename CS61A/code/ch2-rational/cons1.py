# constrctor
# 用python内置的数据类型list来实现有理数的constructor和selector.

def rational(n, d):
	"""
	make a rational num.
	n: numer
	d: denorminator
	"""
	return [n, d]

def num(r):
	"""
	return numer from a rational number.
	r: rational num.
	"""
	return r[0]

def denom(r):
	"""
	return denom from a rational number.
	r: rational num.
	"""
	return r[1]
