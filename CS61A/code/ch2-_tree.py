# constructor & selector
# 基于list实现


"""

1. 用list来构造tree

tree_one = [1]

带一个branches
tree_two = [1, [2]]

带2个branches
tree_three = [1, [2], [1]]


由此可见我们这里把tree定义为带1~3个元素的list. 在这个假设下, 
[1, 2]
不是tree. 因为第二个元素是branch, 根据定义, branch必须是tree, 所以必须是list.


2. 实现:

constructor: 
tree(root, branches[])

selector:
root(tree)
branches(tree)

写完以后, 再进一步加工一下tree(),加入断言和进一步增强. 然后, 再把tree()需要的is_tree()函数也写出来

"""

def tree(root, branches=[]):
	"""
	构建一个tree.

	root: 是数, 也可以是str等
	branches: 若干个tree, 注意要用[]括起来构建成list(这是我们的约定.).

	例如 tree[3, [5]]
	 tree[3, 5] 是不行的
	"""
	for branch in branches:
		if is_tree(branch) != True:
			print('ERROR')
	return [root] + branches

def root(tree):
	"""
	返回一个tree的root值
	"""
	return tree[0]


def branches(tree):
	"""	
	返回一个tree的branches
	例如 [3, [4], [5]]
	返回[[4], [5]]
	外面是有[]包起来的.
	"""	
	return tree[1:]

def is_tree(tree):
	# 先处理当前的tree, 再处理branch. 程序按照短路原则设计: 只要发现任何一个地方不是tree,就返回False, 如果检查完了都发现没有False,就返回True.

	# 输入的tree是一个list吗? 长度一定大于0吗? 如果不是, tree就不满足这里的树的定义
	if type(tree) != list or len(tree) < 1:
		return False

	#  要处理branch了
	for branch in branches(tree):
		if is_tree(branch) == False :
			return False
	return True

def is_leaf(tree):
	"""
	判断tree是否是leaf(没有子树). 是leaf的话就输出True
	"""

	# 输入一个tree, 如果它没有branch了, 肯定就是一个leaf了.
	if not branches(tree):
		return True

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# + barrier
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def print_raw_tree(tree):
	"""
	返回tree的原始数据结构
	"""
	print(str(tree))

def count_leaves(tree):
	"""
	返回tree的leaf的数目
	"""
	# @?@ 如何纯函数式地写一个累加器? 
	if is_leaf(tree):
		return 1
	count = [count_leaves(branch) for branch in branches(tree)]
	return sum(count)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# + barrier
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def fib_tree(n):
	"""
	给定一个树n, 返回一个fib树, 数的node是n, 左支为n-2, 右支为n-1. 子树的node为1或0时终止?
	"""
	# @?@ 不太懂... 这个fib树根本无法保证node的左支是n-2 右支是n-1.
	if n == 0 or n == 1:
	    return tree(n)
	else:
	    left, right = fib_tree(n-2), fib_tree(n-1)
	    fib_n = root(left) + root(right)
	    return tree(fib_n, [left, right])


t1= tree(1)
t2= tree(2)
t3= tree(3)

