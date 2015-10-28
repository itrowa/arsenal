# constrctor
# 直接用来实现有理数的constructor和selector.

def rational(n, d):
	"""
	make a rational num.
	n: numer
	d: denorminator
	"""
	# 虽然说不使用数组， 但是调用ratioal函数,传入的n, d,还是会被保存在这个frame里面
	def dispatch(message):
		if message == 'get-num':
			return n
		elif message == 'get-denom':
			return d
		else:
			print('MESSAGE ERROR')
	return dispatch

def num(r):
	"""
	return numer from a rational number.
	r: rational num.
	"""
	return r('get-num')

def denom(r):
	"""
	return denom from a rational number.
	r: rational num.
	"""
	return r('get-denom')
