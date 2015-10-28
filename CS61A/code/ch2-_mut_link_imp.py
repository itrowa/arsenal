"""
由于Python的抽象屏障, 我们不能直接访问list的实现这一层次, 能访问的只能是 sequence abstraction和 改变list的方法 这个层次.

现在我们要干的事情就是如何用函数和local state来实现list.

实现的时候, 要特别注意identity. 因为任意两个list尽管值相同, identity是不同的.
两个函数, 如果local state都是空的, 足以表明这是两个identity了

先设计一个派包函数(dispatch func), 它的第一个参数就是一个消息. 消息不同, 函数内部就触发不同的操作.
"""


"""
先实现5个功能: len, getitem, push_first, pop_first, str.
"""
from _linked_list import *

def mutable_link():
	"""
	用函数来实现一个可变列表. (对应python的list)
	message passing style
	"""
	contents = empty
	def dispatch(message, value = None):
		nonlocal contents
		if message == 'len':
			# 返回 list长度
			return len_link(contents)
		if message == 'getitem':
			# 返回 list 的指定index位置的元素
			return getitem(contents, value)
		if message == 'push_first':
			# 将元素装入list的第一个位置。
			contents = link(value, contents)
		if message == 'pop_first':
			# 返回列表的的第一个元素 并将列表第一个元素删去。
			contents = rest(s)
			return first(s)
		if message == 'str':
			return print_link(contents)
	return dispatch


# ##################
# 开始利用定义好的list来做一些实际的测试
# ##################

# 创建一个muttable_link()， 内容为空
s = mutable_link()

# 以下是要用来填入list的元素，为了方便起见用py内置的list把它们装起来
raw = ['Alpha', 'Bravo', 'Charlie', 'Delta']

# 先把raw的元素反序， 然后逐个压入s.
for r in reversed(raw):
	s('push_first', r)

print('str test-----------')
print(s('str'))
print('str test end----------- \n')





# ##################################
# 实现python的 dict数据类型
# ##################################

def dictionary():
	"""
	用函数来实现py中dict数据类型。 不过只支持setitem和getitem操作。
	dict是key-value的pair的集合.
	同样的message-passing 风格
	"""
	records = []
	# dict数据内容用Py内置的list类型来保存: 大概是这样:
	# [[key1, value1], [key2, value2], ...]

	def setitem(key, value):
		nonlocal records
		# 思路: records中可能要设置的key是已经存在. 也可能不存在有这个key的pair
		# 所以, 首先把过滤出不对应不上要设置key的pair, 再在records最后追加新的key-value值即可
		nonmatches = [r for r in records if r[0] != key]
		records = nonmatches + [[key, value]]

	def getitem(key):
		matches = [r for r in records if r[0] == key]
		if len(matches) == 1:
			# 这个多重赋值必须以matches的长度为1为前提, 如果matches长度不为1, 多重赋值必须在迭代式中进行
			key, value = matches[0]
			return value


	def dispatch(message, key = None, value = None):
		# 注意setitem这种消息的响应是不用return的
		if message == 'getitem':
			# 通过key 来找value
			return getitem(key)
		elif message == 'setitem':
			# 设置某个key的value 
			setitem(key, value)
	return dispatch

# ##################
# 开始利用定义好的list来做一些实际的测试
# ##################

# 创建一个空的dict
d = dictionary()

# 添加新的pair
d('setitem', 3, 19)
d('setitem', 4, 16)
d('setitem', 'Alpha', 2)

# 根据Key来查找对应的value
d('getitem', 3)
d('getitem', 'Alpha')

