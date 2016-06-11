# 基于binary heap (用数组实现)的优先队列(Max Priority Queue).

class MaxPQ:
    def __init__(self, cap):
        self.l = [None] * cap
        #self.l = [None,1,2,3,4,5,None,None,None,None]
        self.N = 0
        self.cap = cap

    def __repr__(self):
        return self.l.__repr__()

    # 元素的上浮
    def swim(self, k):
        while (k > 1 and self.l[k//2] < self.l[k]):
            self.l[k//2], self.l[k] = self.l[k], self.l[k//2]
            k = k // 2

    # 元素的下沉
    def sink(self, k):
        while (2*k <= N):
            child = 2*k
            # k处的元素要和子级节点的元素中较大的一个交换.

            # 如果子节点左边的小与右边的? 那就把child指针+1
            if (child < self.N and self.l[child] < self.l[child+1]):
                child+=1
            # 让k处元素和药交换的元素先比较大小.
            if (self.l[k] > self.l[child]):
                self.l[k], self.l[child] = self.l[child], self.l[k]
                k = child
            else:
                break

    def insert(self, item):
        self.N+=1
        self.l[self.N] = item
        self.swim(self.N)

    def delMax(self):
        maxItem = self.l[1]
        self.l[maxItem], self.l[N] = self.l[N], self.l[maxItem]
        self.l[N] = None
        self.sink(1)


pq = MaxPQ(10)
pq.insert(6)