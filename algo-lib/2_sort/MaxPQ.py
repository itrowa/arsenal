# 用BinaryHeap实现的Priority Queue

class MaxPQ:
    def __init__(self, cap):
        self.data = [None] * cap 
        self.N = 0

    def __repr__(self):
        return self.data.__repr__()

    # sink the item at index K!
    def sink(self, k):
        while 2*k < self.N:
            if self.data[k] > self.data[2*k] and self.data[k] > self.data[2*k+1]:
            # k处元素本身就比两个都大, 则不用下沉
                break
            elif self.data[2*k] < self.data[2*k+1]:     
            # 右边元素比较大 和右边的交换
                self.data[k], self.data[2*k+1] = self.data[2*k+1], self.data[k]
                k = 2*k + 1
            else:
            # 左边元素比较大 和左边的交换
                self.data[k], self.data[2*k] = self.data[2*k], self.data[k]
                k = 2*k

    # swim the item at index k!
    def swim(self, k):
        while k > 1:
            if self.data[k] > self.data[k//2]:
                self.data[k], self.data[k//2] = self.data[k//2], self.data[k]
                k = k//2
            else:
                break

    # insert an item
    def insert(self, item):
        self.N += 1
        self.data[self.N] = item;
        self.swim(self.N)

    # del an item
    def delMax(self):
        self.data[1], self.data[self.N] = self.data[self.N], self.data[1]
        self.sink(1)
        val = self.data[self.N]
        self.data[self.N] = None
        self.N = self.N - 1
        return val

    def Max(self):
        return self.data[1]

    def size(self):
        return self.N

pq = MaxPQ(20)
pq.insert('S')
pq.insert('O')
pq.insert('R')
pq.insert('T')
pq.insert('E')
pq.insert('X')
pq.insert('A')
pq.insert('M')
pq.insert('P')
pq.insert('L')
pq.insert('E')
