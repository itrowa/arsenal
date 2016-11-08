# 利用二叉查找树建立的符号表

# 实现: 二叉查找树. 每个node储存Key和对应的value, 左树的key小于node, 右树的key大于node.

# 查找: 递归和树的node的key进行比较.然后根据结构再递归到左树或者右树.
# 插入: ...

# @todo: 验证性能; 实现有序ST的其他API: rank(), select(), floor(), keys()

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

    def print(self):
        """ 打印所有的key """
        self.printHelp(self.root)

    def printHelp(self, x):
        """ 中序遍历法 """
        if x == Node.empty:
            return
        else:
            self.printHelp(x.left)
            print(x.key)
            self.printHelp(x.right)

    def size(self):
        return self.sizeHelp(self.root)

    def sizeHelp(self, x):
        """ 返回"""
        if x == Node.empty:
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

        x.N = self.sizeHelp(x.left) + self.sizeHelp(x.right) + 1
        return x

    def deleteMax():
        # 和deleteMin()代码类似.
        pass

    def deleteMin(self):
        """ 删除此树中key最小的node"""
        return self.deleteMinHelp(self.root)
        # note: 对空的二叉树进行此操作将不产生任何效果.

    def deleteMinHelp(self, x):
        """ 删除以node x为根节点的tree的key最小的node."""
        if x.left == Node.empty:
            return x.right
        else:
            x.left = self.deleteMinHelp(x.left)
            x.N = self.sizeHelp(x.left) + self.sizeHelp(x.right) + 1
            return x

    def delete(self, key):
        """ 删除key的node. """
        self.root = self.deleteHelp(key, self.root)

    def deleteHelp(self, key, x):
        """ 删除一个以节点x为根的数中的键为x的node."""
        print("> x is ", x)
        if x == Node.empty:
            return Node.empty
        elif key > x.key:
            x.right = self.deleteHelp(key, x.right)
        elif key < x.key:
            x.left =  self.deleteHelp(key, x.left)
        else : # key == x.key:
            if x.right == Node.empty or x.left == Node.empty:
                return Node.empty
            else:
                t = x
                x = self.minHelp(t.right)
                x.right = self.deleteMinHelp(t.right)
                x.left = t.left
        print("> done! x is ", x)
        x.N = self.sizeHelp(x.left) + self.sizeHelp(x.right) + 1
        return x

    def min(self):
        return self.minHelp(self.root).key

    def minHelp(self, x):
        if x.left == Node.empty:
            return x
        else:
            return self.minHelp(x.left)

    def floor():
        pass

    def ceiling():
        pass

    def keys():
        pass


if __name__ == "__main__":
    # import sys

    # st = BST()

    # keys = sys.stdin.read().split()
    # for i, key in enumerate(keys):
    #     st.put(key, i)

    # print(st)


    # # 对node的测试
    # n1=Node("N",2,1)
    # nn =Node("A", 
    #           1, 
    #           3,
    #           Node("B", 2,1),
    #           Node("C", 3,1)
    #           )

    st = BST()
    st.put("S", 0)
    st.put("E", 1)
    st.put("A", 2)
    st.put("R", 3)
