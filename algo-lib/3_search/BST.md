# BinarySearchTree ST

特点:

- key是有序的


## 其它API

### 最大key / 最小key

最小key:

start from node x:

def findMin(x):
	if x.left is empty:
		return x
	else:
		return algo(x.left)

def findMax(x):
	...

### flooring / ceiling

flooring(key): 求<= key的最大键.

flooring(key, x):
比较key和x.key的大小:
	if key = x.key:
		记录下x.key值
	elif key < x.key:
		flooring(key, x.left)

	elif key > x.key:
		记录下x.key值
		flooring (key, x.right)
	return 记录下的x.key值

flooring(key, x):
	if x is empty: return None
	else:
		if key == x.key:
			return x.key
		elif key < x.key:
			return flooring(key, x.left)
		else: 
			t = floor(x.right, key)
			if t:
				return t
			else:
				return x
当key = x.key时 可直接放回x.key
当key < x.key时, flooring(key)一定在x.left中.
当key > x.key时, flooring(key)可能是x.key 也可能在x.right中.

ceiling(key): 求>= key的最小键.

### rank

select(k): 找到排名为k的键.(树中正好有k个小于它的键.)