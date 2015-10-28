def demo():
	s = 1
	def inner():
		nonlocal s
		s += 2
	return inner

# 以下的代码证明了s +=2 这个语句不能单独成为一个函数来写。

def demo2():
	s = 1
	# 输出现在的s的值
	print(s)
	def inner():
		nonlocal s
		# 这里执行了func(s)后，它能改变这个frame里面的s 的值吗？
		func(s)
		# 执行完后再次输出
		print(s)
	return inner

def func(s):
	s += 2

# 用中括号括住列表推导式会发生什么?
l = [['apple', 5], ['bear', 3], [0, 1], ['charlie', 5], ['delta', 3], [0, 2]]
ll = [r for r in l if r[0] == 0]
# 它会把推导结果的元素用list封装起来.
print(ll)

key, value = l