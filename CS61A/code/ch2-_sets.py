# 1. 利用linked_list实现无序版的set;
# 2. 利用linked_list实现有版的set;
# 3. 利用二叉树实现有序版的set

# 最后需要分析一下3种实现方式的算法复杂度.

# 链表系统.
from _linked_list_object import *

# tree系统
from _tree_obj import *

# ################################
# BinaryTree 为二叉树set做准备.
# ################################
class BinaryTree(Tree):
    """
    在Tree的基础上定义二叉树.

    只有左右两只的Tree.叫做二叉树.
    默认每个树都有分支. 没有实际元素的就用empty表示.
    """
    empty = Tree(None)
    empty.is_empty = True

    def __init__(self, entry, left = empty, right = empty):
        for branch in (left, right):
            assert isinstance(branch, BinaryTree) or branch.is_empty
        Tree.__init__(self, entry, (left, right))
        self.is_empty = False

    @property 
    def left(self):
        return self.branches[0]

    @property 
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return self.left.is_empty and self.right.is_empty

    def __repr__(self):
        if self.is_leaf():
            return 'Bin({0})'.format(self.entry)
        elif self.right.is_empty:
            return'Bin({0},{1})'.format(self.entry, self.left)
        else:
            # @?@ if else是什么语法.... 
            left = 'Bin.empty' if self.left.is_empty else repr(self.left)
            return 'Bin{0}, {1}, {2}'.format(self.entry, left, self.right)

# ################################
# 辅助函数
# ################################

def empty(s):
    """
    测试链表s是不是空的
    """
    return s is Link.empty



# ################################
# UNorderd set implementationa using linked list object 
# ################################


def set_contains(s, v):
    """
    如果一个set s 包含一个元素v则返回True
    """

    if empty(s):
        return False
    elif s.first == v:
        return True
    else: 
        return set_contains(s.rest, v)

def adjoin_set(s, v):
    """
    返回一个set, 里面的元素包含了所有的s的元素和元素v.
    (把元素插入到集)
    """
    # 利用已经造好的轮子
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)


def intersect_set(set1, set2):
    """
    Intersection of set1 and set2.
    返回的集合包含了set1 和 set2的所有元素.
    """
    # 利用filter_link, 找出set1的元素在set2的部分.
    in_set2 = lambda v: set_contains(set2, v)
    return filter_link(in_set2, set1)


def union_set(set1, set2):
    """
    返回set1 和 set2的并集.
    """
    # 找出set1 不在set2的部分, 这部分再和set2合并即可.
    not_in_set2 = lambda v: not set_contains(set2, v)
    set1_not_set2 = filter_link(not_in_set2, set1)
    return extend_link(set1_not_set2, set2)


# ################################
# orderd set implementationa using linked list object 
# ################################

# 假设元素是从小到大排列的.

def set_contains2(s, v):
    """
    如果一个set s 包含一个元素v则返回True
    """
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else: 
        return set_contains2(s.rest, v)

def intersect_set2(set1, set2):
    """
    Intersection of set1 and set2.
    返回的集合包含了set1 和 set2的所有元素.
    """
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            # e1保留在我们要返回的列表中. 剩下的递归处理.
            return Link(e1, intersect_set2(set1.rest, set2.rest))
        if e1 < e2:
            # 抛弃掉e1, 因为e1和e2并不相等. 而且e1不可能再和set2的其它元素相等了.
            return Link(e1, intersect_set2(set1.rest, set2))
        if e1 > e2:
            # 抛弃掉e2
            return Link(e1, intersect_set2(set1.rest, set2))



# 利用二叉搜索树实现集合..

def set_contains3(s, v):
    if s.is_empty:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return set_contains3(s.right, v)
    elif s.entry > v:
        return set_contains3(s.left, v)

def adjoin_set3(s, v):
    if s.is_empty:
        return Binerytree(v)
    elif s.entry == v:
        return s
    elif s.entry < v:
        # 构建二叉树, 用新的左支不变, 右支用新的
        return BineryTree(s.entry, s.left, adjoin_set3(s.right, v))
    elif s.entry > v:
        return BineryTree(s.entry, adjoin_set3(s.left, v), s.right)

def big_tree(left, right):
    """
    返回一个二叉搜索树, 元素是left到right的中间值.
    >>> big_tree(0, 12)
    Bin(6, Bin(2, Bin(0), Bin(4)), Bin(10, Bin(8), Bin(12)))
    """
    if left > right:
        return BinaryTree.empty
    elif left == right:
        return BinaryTree(left)
    split = left + (right - left) // 2
    return BinaryTree(split, big_tree(left, split - 2), big_tree(split + 2, right))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# abstraction barrier
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# ################################
# Test
# ################################

s = Link(1, Link(2, Link(3)))
set_contains(s, 3)
set_contains2(s, 3)
