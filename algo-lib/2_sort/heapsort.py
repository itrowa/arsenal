# 利用二叉堆给"array"排序  array 从1号位置开始.
# 1st pass: 把array想象成一个非有序二叉堆, 这一步的目的是构建堆有序
# 2nd pass: 递归利用sink()给子堆排序.

# @todo: 需要完全二叉树。好像有些长度的数组形成不了完全二叉树。例如1 2 3 4 5 6 7 8 9 一旦计算第5号元素的child
# 数组立马元素溢出. 得解决这个问题 (教材上也没解决这个问题)

from MaxPQ import MaxPQ, pq

def sort(pq):
    # 1st pass:
    for k in range(pq.N // 2, 0, -1):
        pq.sink(k)

    # 2nd pass:
    while(pq.N>1):
        pq.data[1], pq.data[pq.N] = pq.data[pq.N], pq.data[1]
        # a[N-1], a[1] = a[1], a[N-1]
        pq.N -= 1
        pq.sink(1)

# test
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
sort(pq)
