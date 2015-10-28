# 基于线性探测法的Hash表

# 实现: 两队平行数组, 一个存储keys, 一个存储values, 遇到冲突项, 往指针变大的方向继续放.

# @todo: 验证get和delete的正确性; , 数组动态扩展, 验证性能

class LinearProbingHashST:

    def __init__(self, M=16):
        self.N = 0                              # key-value pair的个数
        self.M = M                              # 取一个固定值(在例子中就是16)
        self.keys = [None] * self.M                  # 存放keys 的数组
        self.values = [None] * self.M                # 存放values 的数组

    def __repr__(self):
        s = ""
        for i in range(0, self.M):
            s += repr(i).rjust(6)
        s += "\n"
        for i, item in enumerate(self.keys):
            # s += "{!s:5}".format(item)
            s += repr(item).rjust(6)
        s += "\n"
        for i, item in enumerate(self.values):
            # s += "{!s:5}".format(item)
            s += repr(item).rjust(6)
        # s += self.keys.__repr__() + "\n"
        # s += self.values.__repr__()
        return s

    def delete(self, key):
        i = self.gethash(key)

        def i_next(i):
            # 计算下标i的下一项.
            return (i+1) % self.M

        # while循环: 从i开始查找对应项, 如找到就执行删除并左移
        # 剩余的同hash key, 若一直查找到None则证明无此key.
        while(self.keys[i] != None):
            if self.keys[i] == key:
                #直接删除
                self.values[i] = None
                #把右边同hash的key左移
                while self.keys(i_next(i)) != None:
                    self.keys[i] = self.keys[i_next]
                    self.values[i] = self.values[i_next]
                    i = i_next(i)
                return
            i = (i + 1) % self.M

    def get(self, key):
        i = self.gethash(key)
        while(self.keys[i] != None):
            if key == self.keys[i]:
                return self.values[i]
            i = (i+1) % self.M
        return None
        

    def put(self, key, value):
        """
        put at index i if free; if not try i+1, i+2,... and loop back to 0, 1,..etc
        """
        # 注意先resize
        # if (self.N >= self.M/2):
        #     resize(2*self.M)

        index = self.gethash(key)
        # 1. index位置元素为空, 直接放入
        # 2. index位置元素key相同, 更新value
        # 3. index位置元素key不同, 继续寻找index+1的元素
        while(self.keys[index] != None):
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.M        # 之所以不用index+=1是因为当index到了超过15的时候,
                                                # 下一个index又可以回到0,1,2,..
        self.keys[index] = key
        self.values[index] = value
        self.N += 1

    def resize(self, cap):
        pass

    def gethash(self, key):
        """
        将python的hash返回值转换为我们需要的数组索引. 数组索引范围为0~(M-1), 共M个.
        """
        return (hash(key) & 0x7fffffff) % self.M
        # 剔除符号位.

if __name__ == "__main__":
    lphst = LinearProbingHashST()       # 课本上的例子就是长度为5
    lphst.put("S", 0)
    lphst.put("E", 1)
    lphst.put("A", 2)
    lphst.put("R", 3)
    lphst.put("C", 4)
    lphst.put("H", 5)
    lphst.put("E", 6)
    lphst.put("X", 7)
    lphst.put("A", 8)
    lphst.put("M", 9)
    lphst.put("P", 10)
    lphst.put("L", 11)
    lphst.put("E", 12)