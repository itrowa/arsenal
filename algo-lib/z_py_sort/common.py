# 是第几个元素下标就是几，操作数组实际下标的dirty job被exch和less函数封装起来了.
# 这就是cs理论中的思考方式.

l = ["S","O","R","T","E","X","A","M","P","L","E"]
# len = 11

# exch(l, 2, 3)
# 交换l的2,3号元素

def less(a, i, j):
    return a[i-1] < a[j-1]

def exch(a, i, j):
    a[i-1], a[j-1] = a[j-1], a[i-1]
