# python来实现tree
# tree 的一些操作: simplified version
"""

首先我们是想要利用list来实现tree的数据结构. 下一步就是考虑写怎样的函数能够操作list. 就像上次写有理数的结构一样.

constructor: 
tree(root, branches[])

selector:
root(tree)
branches(tree)

写完以后, 再进一步加工一下tree(),加入断言和进一步增强. 然后, 再把tree()需要的is_tree()函数也写出来
"""



def tree(root, branches=[]):    # brunches参数的默认值是:[]
    """
    constructor: 用root和branches来构建一个树。
    """
    #assert断言是为了进一步确定它是一个tree
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)             #为何要用list()? 同样是为了保险起见, 把branches加工成list.


def root(tree):
    """
    root(tree) = 'root of a tree', 这样读函数会容易很多.
    返回一个tree的根节点

    """
    return tree[0]


def branches(tree):
    """
    branches of a tree
    这些branch是用[]括起来的
    """
    return tree[1:]

def is_tree(tree):
    """
    判断输入的东西是否是树
    """
    # tree根本不是list, 或者tree的长度小于1.(连node值都没了) 那就肯定不是tree了
    if type(tree) != list or len(tree) < 1: 
        return False

    # tree的每个branche也要是tree.否则这个tree不是tree.
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    # 一个tree中没有branch,那么就是leaf.
    return not branches(tree)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# abstraction barrier
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 下面的函数是根据上面层级来实现的.

# ###########
# fib_tree.
# ###########

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = root(left) + root(right)
        return tree(fib_n, [left, right])
# >>> fib_tree(5)
# [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]

# ###########
# 给treee实现更多的count功能
# ###########

def count_leaves(tree):
    """The number of leaves in tree.

    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)

def leaves(tree):
    """The leaf values in tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [root(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

# ############################
# partition tree / 换零钱问题的树
# ############################

def partition_tree(n, m):
    """
    Return a partition tree of n using parts of up to m.
    返回的数中,左边的子树表示是用到最多m来分上一级树,右边是不用m来分的结果.
    如果树节点为true,表示分割成功,false表示分隔失败
    树的节点的数字表示是用最大为这个数字来分隔,若有子树,子树就表示用这个树分隔..

    """
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])
# >>> partition_tree(2, 2)
# [2, [True], [1, [1, [True], [False]], [False]]]
# 记得用几个例子测试一下, 把结果画成图形
#                      2
#             __________________
#             |                |
#             true             1
#                          __________
#                         |          |
#                         1        false
#                      _______
#                      |     |
#                     true  false




def print_parts(tree, partition=[]):
    # 怎么去思考? 把partition tree画出来, 看看哪些节点相加得到正确的分隔值就有思路了.

    # 递归终止条件~
    if is_leaf(tree): # 如果tree没有子树
        if root(tree): # 如果tree的root为True.(前面的partition tree的所有leaf不是true就是false,这一句正是为了筛选那些True的分支)
            print(' + '.join(partition))       # 为什么有我不懂的语法...

    # 如果不是树叶 那么要继续递归
    else:
        left, right = branches(tree)           # 把左右两只branch分别绑定给left, right
        m = str(root(tree))
        print_parts(left, partition + [m])     # 递归调用自己, 同时, partition 一直在记录往下遍历时每个树的root值, 同时注意对左支遍历的时候, 要加上这个树的root值, 而对右边递归的时候则不用. 这是因为右边那一只不用最大为root的那个数来做partition.
        print_parts(right, partition)

# >>> print_parts(partition_tree(6, 4))


