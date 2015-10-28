# encoding: utf-8

# def name(f):
# 	return <exp>

# 要这样理解： 创建一个函数lambda: 采取参数f 返回<exp> 最后给这个函数命名为name


def zero(f):
	return  lambda x: x 

# 给zero(f) 传入一个参数例如cos 
# 则返回一个结果 lambda x: x

def one(f):
	return lambda x: f(x)

# 这里如果给one(f)传入一个实际参数例如cos.
# 则返回一个lambda x: cos(x)
# 要再传入一个参数x 才能计算出结果， 例如 pi

def two(f):
	return lambda x: f(f(x))

# 由是, 发现规律， 直接定义一个可以递推的函数， 用two(f)传进去就能得到three
def successor(num):
	# return: num    相当于什么都没干 直接返回num
	# return num(f)(x)  相当于得到f(f(x)), 注意这个写法是错的，因为前面还有lambda f: lambda x: 两层嵌套
	# return f(num(f)(x)) 相当于得到 f(f(f(x)))

	return lambda f: lambda x: f(num(f)(x))

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    return n(lambda x: x + 1)(0)