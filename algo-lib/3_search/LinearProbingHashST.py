# Symbol Table: 基于线性探测法的Hash表

# 实现: 两队平行数组, 一个存储keys, 一个存储values, 遇到冲突项, 往指针变大的方向继续放.
# 数组大小动态扩展: 总是让占用率在1/8 ~ 1/2之间.

# @todo: 验证正确性!

class LinearProbingHashST:

    def __init__(self, M=4):
        self.N = 0                              # 已存放的数据(key-value pair)的个数
        self.M = M                              # 线性探测表的长度 . 取一个固定值(对动态数组, 是4)
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
        if (not self.contains(key)):
            return None
        i = self.gethash(key)

        while(self.keys[i] != key):     # 找到存储要删除的key的数组下标
            i = (i + 1) % self.M

        self.keys[i] = None             # 将要删除的key和value的数组元素置空
        self.values[i] = None
        i = (i + 1) % self.M
        while self.keys[i] != None:          # 针对key的下标后面的每个数据:
            keyToRedo = self.keys[i]         # 将数据置空 并重新put此数据
            valToRedo = self.values[i]
            self.keys[i] = None
            self.values[i] = None
            self.N -= 1
            self.put(keyToRedo, valToRedo)
            i = (i + 1) % self.M
        self.N =- 1

        if self.N > 0 and self.N == self.M // 8:
            resize(self.M // 2)
        # note: 保证线性探测表的占用率不低于1/8.

    def get(self, key):
        i = self.gethash(key)
        while(self.keys[i] != None):
            if key == self.keys[i]:
                return self.values[i]
            else:
                i = (i+1) % self.M
        return None
        

    def put(self, key, value):
        """ put at index i if free; if not try i+1, i+2,... and loop back to 0, 1,..etc
        """
        if (self.N >= self.M/2):
            self.resize(2*self.M)
        # note: 保证线性探测表的占用率不超过1/2.

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

    def contains(self, key):
        return self.get(key) != None

    def resize(self, cap):
        """ 将keys[]和values[]扩大或者缩小到指定长度. """
        t = LinearProbingHashST(cap)
        for i in range(self.M):
            if(self.keys[i] != None):
                t.put(self.keys[i], self.values[i])
            self.keys = t.keys
            self.values = t.values
            self.M = t.M
        # note: 不能直接复制数组 而要用put 方法, 因为key的hash值取决于线性探测表数组的大小.
        # 线性探测表长度变化后, 所有的数据都要重新进行put操作.

if __name__ == "__main__":
    st = LinearProbingHashST()       # 课本上的例子就是长度为5
    # st.put("S", 0)
    # st.put("E", 1)
    # st.put("A", 2)
    # st.put("R", 3)
    # st.put("C", 4)
    # st.put("H", 5)
    # st.put("E", 6)
    # st.put("X", 7)
    # st.put("A", 8)
    # st.put("M", 9)
    # st.put("P", 10)
    # st.put("L", 11)
    # st.put("E", 12)