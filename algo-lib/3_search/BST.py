# 利用二叉查找树建立的符号表

# 实现: 二叉查找树. 每个node储存Key和对应的value, 左树的key小于node, 右树的key大于node.

# 查找: 递归和树的node的key进行比较.然后根据结构再递归到左树或者右树.
# 插入: ...


# @todo: 验证性能; 实现有序ST的其他API.


class Node:
    # 这个class将被BST class直接使用.
    def __init__(self, key, value, N, left=None, right=None):       # hint: N必须放在有默认值参数的前面.
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
    def __init__(self, key, value):
        # 初始化一个tree节点 self.t就是引用整个BST树的变量了
        self.t = Node(key, value, 1)

    def __repr__(self):
        return self.t.__repr__()

    def size(self):
        return self.size_core(self.t)

    def size_core(self, n):
        if not n:
            return 0
        else:
            return n.N

    def get(self, key):
        # 一个外壳函数, 调用真正的get_core()
        return self.get_core(self.t, key) 

    def get_core(self, n, key):
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
        # 调用self.put_core()更新红黑树的值.
        self.t = self.put_core(self.t, key, value)


    def put_core(self, n, key, value):
        # 如果key存在于以某个node为root的tree中则更新其value,否则就新建一个节点.
        # 递归式运行.

        # base case: 节点n是空, 返回一个新建的节点.
        if (n == None):
            return Node(key, value, 1)
        # 要put的小于root的key时:
        if (key < n.key):           
            n.left = self.put_core(n.left, key, value)
        # 要put的大于root的key时:
        elif(key > n.key):
            n.right = self.put_core(n.right, key, value)
        # 要put的等于root的key时:
        else:
            n.value = value
        n.N = self.size_core(n.left) + self.size_core(n.right) + 1
        return n

if __name__ == "__main__":
    # 对node的测试
    n1=Node("N",2,1)
    nn =Node("A", 
              1, 
              3,
              Node("B", 2,1),
              Node("C", 3,1)
              )

    # 对BST的测试
    st = BST("N", 1)
    st.put("B", 2)
    st.put("Z", 3)
    st.put("X", 4)
    st.put("Y", 5)
    st.put("C", 6)
    st.get("B")
    st.get("Z")
