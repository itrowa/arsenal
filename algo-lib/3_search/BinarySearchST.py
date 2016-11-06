# 利用对数组进行二分查找的方式完成符号表功能.

# 数据结构实现：一对平行的数组，一个存储keys的值，一个存储value的值. key数组中的key是有序的. 而查找key则使用二分查找法.

# 二分查找(rank()函数): 在数组中引入low, mid, hi 3个指针, 把要比较的key和mid处的key比较, 然后得到了
# 包含key所在的区间, 于是把另外一半扔掉. 继续递归, 直到遇到key和mid相等,或者...

# 插入: 先通过rank()找到当前key要插入的位置, 执行更新或者选择插入(先把右侧元素全部右移一个位置,形成空位再插).

# @todo: 未做完.

class BinarySearchST:

    def __init__(self, capacity):
        self.keys, self.vals = [None] * capacity
        self.N = 0                                          # size, not array size!

    # return st size.
    def size(self):
        return N

    # 查找给定的key并返回对应的value
    def get(self, key):
        if (isEmpty()) return None
        i = self.rank(key)
        if (i < self.N and self.keys[i] == key):
            return self.vals[i]
        else:
            return None

    def put(self, key, val):
        i = self.rank(key)
        if (i < self.N and self.keys[i] == key):
            vals[i] = val
            return
        # 在原来的数组中找不到key. 因此插入至合适位置.
        for j in range(N, -1, i):
            self.keys[j] = self.keys[j-1]
            self.vals[j] = self.vals[j-1]
        self.keys[i] = key
        self.vals[i] = val
        self.N += 1

    # def delete(key):
    # @todo


    # 返回比key小的key的数量.
    def rank(self, key):
        lo, hi = 0, N-1
        while (lo <= hi):
            mid = lo + (hi - lo) // 2
            if (key < self.keys[mid]):
                hi = mid - 1
            elif (key > self.keys[mid]):
                lo = mid + 1
            else:
                return mid
        return lo

    def min(self):
        return keys[0]

    def max(self):
        return keys[N-1]

    def select(self, k):
        return keys[k]