# 单向链表
class Node:
	def __init__(self, val, next = None):
		self. val = val
		self.next = next


# 双向链表
class doubleNode:
	def __init__(self, val, next = None, prev = None):
		self.val = val
		self.next = next
		self.prev = prev

# 循环链表 (* 面试中很少出现.)