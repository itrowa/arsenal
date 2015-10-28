class Tree:
    """Tree. 包t
    """
    def __init__(self, entry, branches=()):
        # branches 一定是要用tuple包起来的.
        self.entry = entry
        for branch in branches:
            # 验证branch的每一支都是满足tree class的对象.
            assert isinstance(branch, Tree)
        # 强制转换成list.
        self.branches = list(branches)
        
    def __repr__(self):
        if self.branches:
            # 如果self.branches存在
            branches_str = ', ' + repr(self.branches)
        else:
            # 如果self.branches是空
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def is_leaf(self):
        return not self.branches
        
# ===================================
# tree的一些实例
# ===================================

# fibonacci tree

def fib_tree(n):
    """ fibonacci tree.

    >>> fib_tree(4)
    Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    """
    #  如果搞不懂, 可以先以fib_tree(2) 为例子; 再研究fib_tree(3)
    if n == 0 or n == 1:
        return Tree(n)
    else:
        # 分别创建左支和右支的tree.
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        # 最后构建用算好的左支,右支作为tree的branch参数, tree的value就是左支的root与右支的root之和, 最后构建tree.
        return Tree(left.entry + right.entry, (left, right))

# hailstone tree

def hailstone(n):
    """ 对给定的n, 打印对应的hailsone数列, 然后返回它的长度.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n*3 + 1)

# 帮助haistone tree的辅助函数

def is_int(x):
    return int(x) == x

def is_odd(n):
    return n % 2 == 1

def hailstone_tree(k, n=1):
    """ 生成一个tree来表示hailstone数列的各种可能性.
    k是树的深度; n是从几开始作为n创建hailstone数列

    树是倒着考虑的. 先是从n(默认为1)开始(这就是tree的root, 下一步根据hailstone规则生成下一个数, 如果有多种可能性, 就有多个branches.
    """
    if k == 1:
        return Tree(n)
    else:
        # 对于给定的n 下一步有两种选择.
        more = 2*n
        less = (n-1)/3

        # 利用一个list来记录branch.
        branches = []

        branches.append(hailstone_tree(k-1, more))
        if less > 1 and is_int(less) and is_odd(less):
            branches.append(hailstone_tree(k-1, less))

    return Tree(n, branches)

# def leaves(tree):

# def longest_path_below(k, t):

