# 利用二叉查找树建立的符号表

# 实现: 二叉查找树. 每个node储存Key和对应的value, 左树的key小于node, 右树的key大于node.

# 查找: 递归和树的node的key进行比较.然后根据结构再递归到左树或者右树.
# 插入: ...

# @todo: 验证性能; 实现有序ST的其他API. 例如 del

# test: python -i BST < tinyST.txt
 # *  A 8
 # *  C 4
 # *  E 12
 # *  H 5
 # *  L 11
 # *  M 9
 # *  P 10
 # *  R 3
 # *  S 0
 # *  X 7

class Node:
    empty = () # 用于标记空的node， 以及空的val, value.
    # 这个class将被BST class直接使用.
    def __init__(self, key, value, N, left=empty, right=empty):       # hint: N必须放在有默认值参数的前面.
        self.key = key                          # key
        self.value = value                      # value
        self.left = left                        # 指向左子树的指针
        self.right = right                      # 指向右子树的指针
        self.N = N                              # 以该节点为root的子树的节点总数

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
        return "Tree([{0}:{1}] {2} {3})".format(self.key, self.value, left_str, right_str)


class BST:
    def __init__(self,):
        """ 创建一个空的BST对象. """
        # 初始化根节点. empty是哨兵. 树为空时的状态.
        self.root = Node.empty

    def __repr__(self):
        return self.root.__repr__()

    def size(self):
        return self.size_help(self.root)

    def size_help(self, x):
        """ 返回"""
        if not x:
            return 0
        else:
            return x.N

    def get(self, key):
        # 一个外壳函数, 调用真正的get_core()
        return self.get_core(self.root, key) 

    def get_core(self, x, key):
        # 先处理n是空tree的情况避免浪费表情
        if (x == None):
            return None
        # n非空，可以让传入的key和n的key比较了.
        while (x != None):
            if(key < x.key):
                return self.get_core(x.left, key)
            elif(key > x.key):
                return self.get_core(x.right, key)
            elif(key == x.key):
                return x.value

    def put(self, key, value):
        # 调用self.put_core()更新红黑树的值.
        self.root = self.put_core(self.root, key, value)


    def put_core(self, x, key, value):
        # 如果key存在于以某个node x为root的tree中则更新其value,否则就新建一个节点.
        # 递归式运行.

        # base case: 节点x是空, 返回一个新建的节点.
        if (x == Node.empty):
            return Node(key, value, 1)
        else:
            if (key < x.key):           
                x.left = self.put_core(x.left, key, value)
            elif(key > x.key):
                x.right = self.put_core(x.right, key, value)
            else:
                x.value = value

        x.N = self.size_help(x.left) + self.size_help(x.right) + 1
        return x

    def deleteMax():
        pass

    # @todo: correctness check! 
    def deleteMin(self, x):
        """ 删除此树中key最小的node"""
        return self.deleteMinHelp(root)

    def deleteMinHelp(self, x):
        """ 删除以node x为根节点的tree的key最小的node."""
        if x.left == Node.empty:
            return x.right
        else:
            x.left = deleteMin(self, x.left)
            x.N = self.size(x.left) + self.size(x.right) + 1
            return x

    # @todo: correctness check!
    def delete(self, key):
        """ 删除key的node. """
        self.root = self.deleteHelp(key, root)

    def deleteHelp(self, key, x):
        """ 删除一个以节点x为根的数中的键为x的node."""
        if x == Node.empty:
            return Node.empty
        elif key == x.key:
            if x.right == Node.empty or x.left == Node.empty:
                return Node.empty
            else:
                t = x
                x = self.min(t.right)
                x.right = self.deleteMinHelp(t.right)
                x.left = t.left
                return x
        elif key > x.key:
            return self.deleteHelp(self, key, x.right)
        else:
            return self.deleteHelp(self, key, x.left)

    # @todo: correctness test
    def min(self):
        return self.minHelp(x)

    def minHelp(self, x):
        if x.left == null:
            return x
        else:
            return minHelp(self, x.left)

    def floor():
        pass

    def ceiling():
        pass

    def keys():


if __name__ == "__main__":
    import sys

    st = BST()

    keys = sys.stdin.read().split()
    for i, key in enumerate(keys):
        st.put(key, i)

    print(st)


    # 对node的测试
    n1=Node("N",2,1)
    nn =Node("A", 
              1, 
              3,
              Node("B", 2,1),
              Node("C", 3,1)
              )

