# #####################################################
# 循环链表
# #####################################################

# 当一个链表的末尾指向链表本身时会发生什么?
def cycle_demo():
    """A linked list can contain cycles.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first = 5
    >>> t = s.rest
    >>> t.rest = s
    >>> s.first
    5
    >>> s.rest.rest.rest.rest.rest.first
    2
    """



# #####################################################
# Bear environment
# #####################################################

# ...
def oski(bear):
    """Oski the bear.

    >>> oski(abs)
    [2, [3, 1]]
    """    
    # 对于上面那个, 用环境模型一分析就知道了.
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [bark+1, berk-1]
        bear = lambda lay: berk - ley
        return [berk, cal(berk)]
    return cal(2)

# #####################################################
# Worker and bourgeoisie
# #####################################################

class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'My job is to gather wealth'

# 一个关于python class 和 instance的综合练习, 注意两个类之间的继承和class attr, instance attr就可以了.
jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Mamm'

def work():
    # 把下面这些运行的结果搞懂就行了.
    
    """working.
    >>> Worker().work()
    'Sir, I work'
    >>> jack
    Peon
    >>> jack.work()
    'Maam, I work'
    >>> john.work()
    Peon, I work
    'My job is to gather wealth'
    >>> john.elf.work(john)
    'Peon, I work'
    """
 

# #####################################################
# Morse Code
# #####################################################

# 首先要有一个morse字典, 记录编码和字母的关系.
abcde = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.'
}


# 通过morse(abcde)函数把abcde变成莫尔斯编码的二叉树(通过., - 来查找字母)
from _tree_obj import *
from _linked_list_object import *

class BinaryTree(Tree):
    """
    二叉搜索树
    """
    # 建立一个空的Tree实体
    empty = Tree(None)
    # 并且设置instance attr
    empty.is_empty = True

    def __init__(self, entry, left = empty, right = empty):
        for branch in (left, right):
            assert isinstance(branch, BinaryTree) or branch.is_empty
        # 调用它父类的__init__函数
        Tree.__init__(self, entry, (left, right))
        # 并且设置instance attr.
        self.is_empty = False

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def __repr__(self):
        if self.left.is_empty and self.right.is_empty:
            return 'Bin({0})'.format(self.entry)
        elif self.right.is_empty:
            return 'Bin({0}), {1})'.format(self.entry, self.left)
        else:
            left = 'bin.empty' if self.left.is_empty else repr(self.left)
            return 'Bin({0}, {1}, {2})'.format(self.entry, left, self.right)

    def is_leaf(self):
        return self.left.is_empty and slef.right.is_empty

def ensure(tree, k):
    """
    检查tree的分支k不是空的.
    如果是空的, 就用空格作为tree的entry值
    """
    if tree.branches[k] is BinaryTree.empty:
        tree.branches[k] = BinaryTree(' ')
    return tree.branches[k]

def morse(code):
    """
    给出一个莫尔斯电码的字典, 就返回一个莫尔斯的二叉树.(用电码来找字母)
    """
    # 先建立一个值为空格的二叉树
    root = BinaryTree(' ')
    # 读取字典
    for letter, signals in abcde.items():
        # 换个名字
        branch = root
        # 决定这个tree的左
        for signal in signals:
            if signal == '.':
                branch = ensure(branch, 0)
            elif signal == '-':
                branch = ensure(branch, 1)
        branch.entry = letter
    return root

# 通过decode('morse string', 'morse_tree') 来把一段莫尔斯码通过查找morse_tree的方式解码成字母.
def decode(signals, tree):
    """
    把signal解码为英文字母. tree是用来查找用的莫尔斯二叉树.

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        if signal == '.':
            tree = tree.left
        elif signal == '-':
            tree = tree.right
    return tree.entry