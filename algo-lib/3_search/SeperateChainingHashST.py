# 基于拉链法的hash表

# hash函数: 把所有要装入M个槽位的key计算出hash值, 并使它们均匀分布在M个槽位中. 详细见书.
# 碰撞处理: 拉链法. 把发生冲突的元素放入链表中.

# 实现:
# 使用N个key-value对装入大小为M的数组st. 数组的每个元素都指向一个SequentialSearchST类的链表,
# 每次计算要插入的key的hash并作为数组st的index装入st的对应位置. 若有新的的key的hash值在st的同样的下标
# , 按SequentialSearchST的put()方法继续插入即可.

# python实现的难点:
# 把初始化后的list装入M个空的SequentialSearchST的空对象.

# @todo: get()

from SequentialSearchST import *

class SeperateChainingHashST:
    def __init__(self, M):
        self.M = M                      # hash表大小
        self.st = [None] * M                     # 一个"数组"用于符号表, 固定长度, 为M

    def __repr__(self):
        """
        get things like...
        [0] : STNode(P: 10, STNode(M: 9, STNode(H: 5, STNode(A: 8))))
        [1] : STNode(L: 11, STNode(X: 7))
        [2] : STNode(R: 3, STNode(E: 12, STNode(S: 0)))
        [3] : None
        [4] : STNode(C: 4)
        """
        s = ""                  # output string
        st = self.st
        for i, item in enumerate(st):
            if item == []:
                s += "[{0}] : None\n".format(i)
            else:
                s += "[{0}] : {1}\n".format(i, item.__repr__())
        return s

    def put(self, key, value):
        index = self.gethash(key)
        item = self.st[index]
        if item == None:
            self.st[index] = SequentialSearchST(key, value)
        else:
            self.st[index].put(key, value)


    def get(self, key):
        return self.st[self.gethash(key)].get(key)

    def gethash(self, key):
        """
        将python的hash返回值转换为我们需要的数组索引. 数组索引范围为0~(M-1), 共M个.
        """
        return (hash(key) & 0x7fffffff) % self.M
        # 剔除符号位.

# test client
if __name__ == "__main__":
    schst = SeperateChainingHashST(5)       # 课本上的例子就是长度为5
    schst.put("S", 0)
    schst.put("E", 1)
    schst.put("A", 2)
    schst.put("R", 3)
    schst.put("C", 4)
    schst.put("H", 5)
    schst.put("E", 6)
    schst.put("X", 7)
    schst.put("A", 8)
    schst.put("M", 9)
    schst.put("P", 10)
    schst.put("L", 11)
    schst.put("E", 12)

    # note: 应注意E的值被更新了多次, 完成后应是12.
