# 引用透明性 demo


def f(x):
	x = 4
	def g(y):
		def h(z):
			nonlocal x
			x = x + 1
			return x + y + z
		return h
	return g

a = f(1)
b = a(2)
total = b(3) + b(4)

# 如果最后一句修改为total = 10 + b(4)
# 尽管b(3)的结果就是10, 但是total的结果和之前的tatal还是不一样. 因为b(3)在执行过程中, 除了返回10以外, 还通过nonlocal声明, 额外改变了它的上一级frame中的x的值, 也就是说,它改变了环境.带来了副作用. referential transparency 丢失了.