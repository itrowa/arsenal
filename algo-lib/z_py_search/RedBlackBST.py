## Red-Black Tree symbol table.
# 保持完美平衡.

# 实现: 把红黑树看成是2-3树的一种实现. 

# @todo: 未完成; delete()函数, 如何做到只"声明"不初始化

RED = True
BLACK = False

class Node:
    """
    表示一个红黑树Node的class.
    """
    def __init__(self, key, value, N, color, left=None, right=None):
        self.key = key                      # key
        self.value = value                  # value
        self.N = N                          # 此Node为root时的节点数目统计.
        self.color = color                  # 此Node的颜色(实际上是父节点到此节点的链接的颜色)
        self.left = left                    # left子树
        self.right = right                  # right子树

    def __repr__(self):
        """
        打印方法..
        """
        if self.left == None:
            left_str = "()" 
        else: 
            left_str = repr(self.left)
        if self.right == None:
            right_str = "()" 
        else: 
            right_str = repr(self.right)

        # 最终输出..
        if self.color == RED:
            return "RT([{0}|{1}] {2} {3})".format(self.key, self.value, left_str, right_str)
        elif self.color == BLACK:
            return "BT([{0}|{1}] {2} {3})".format(self.key, self.value, left_str, right_str)

class RedBlackBST:
    """
    红黑树class. 
    self.t存储了红黑树本身; 剩下的关于红黑树的一些方法.
    """
    # st = RedBlackBST("B", 2)
    # st.t   打印BST
    # st.t.key
    # st.t.value
    # st.key.left.key
    # ...
    def __init__(self, key, value):
        self.t = Node(key, value, 1, BLACK)

    def __repr__(self):
        return self.t.__repr__()

    def isRed(self, n):
        """
        判断一个node n是否是红色.
        """
        if not n:
            return False
        return n.color == RED

    def rotateLeft(self, h):
        """
        旋转node h处的右链接到左边. 并返回旋转后的树.
        """
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED 
        x.N = h.N
        h.N = 1 + self.size_node(h.left) + self.size_node(h.right)
        return x

    def rotateRight(self, h):
        """
        旋转node h处的左链接到右边. 并返回旋转后的树.
        """
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        x.N = h.N
        h.N = 1 + self.size_node(h.left) + self.size_node(h.right)
        return x

    def flipColors(self, h):
        """
        转换node h处的颜色.
        """
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

    def size(self):
        """
        返回整个树的大小.(节点数)
        """
        if not self.t:
            return 0
        else:
            return self.t.N

    def size_node(self, n):
        """
        返回node n 为根节点时树的大小(节点数)
        """
        if not n:
            return 0
        else:
            return n.N

    def get(self, key): 
        """
        返回整个树的大小
        """
        # 一个外壳函数, 调用真正的get_core()
        # note: get方法和二叉树的完全一样. 红黑树在查找时完全可以当作二叉树看待.
        return self.get_core(self.t, key) 

    def get_core(self, n, key):
        """
        返回以node n作为根节点时key对应的value.
        """
        # note: get方法和二叉树的完全一样. 红黑树在查找时完全可以当作二叉树看待.
        
        # 先处理n是空tree的情况避免浪费表情
        if (n == None):
            return None
        # n非空，可以让传入的key和n的key比较了.
        while (n != None):
            if(key < n.key):
                return self.get_core(n.left, key)
            elif(key > n.key):
                return self.get_core(n.right, key)
            elif(key == n.key):
                return n.value

    def put(self, key, value):
        """
        将一对key-value pair 插入到树中
        """
        # 调用self.put_core()更新红黑树的值.
        self.t = self.put_core(self.t, key, value)
        self.t.color = BLACK

    def put_core(self, n, key, value):
        """
        将一对key-value pair 插入到节点n为根节点的红黑树中.
        """
        # 如果key存在于以某个node为root的tree中则更新其value,否则就新建一个节点.
        # 递归式运行.

        # base case: 节点n是空, 返回一个新建的节点, 和父节点用红色链接相连.
        if (n == None):
            return Node(key, value, 1, RED)

        # 要put的小于root的key时:
        if (key < n.key):           
            n.left = self.put_core(n.left, key, value)
        # 要put的大于root的key时:
        elif(key > n.key):
            n.right = self.put_core(n.right, key, value)
        # 要put的等于root的key时:
        else:
            n.value = value

        # 针对红黑树新增的部分:
        if (self.isRed(n.right) and not self.isRed(n.left)):
            n = self.rotateLeft(n)
        if (self.isRed(n.left) and self.isRed(n.left.left)):
            n = self.rotateRight(n)
        if (self.isRed(n.left) and self.isRed(n.right)):
            self.flipColors(n)
        n.N = self.size_node(n.left) + self.size_node(n.right) + 1
        return n

if __name__ == "__main__":
    rbt = RedBlackBST("S", 0)
    rbt.put("E", 1)
    rbt.put("A", 2)
    rbt.put("R", 3)
    rbt.put("C", 4)
    rbt.put("H", 5)
    rbt.put("E", 6)
    rbt.put("X", 7)
    rbt.put("A", 8)
    rbt.put("M", 9)
    rbt.put("P", 10)
    rbt.put("L", 11)
    rbt.put("E", 12)