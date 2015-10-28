# 利用二叉堆给"array"排序  array 从1号位置开始.
# 1st pass: 把array想象成一个非有序二叉堆, 这一步的目的是构建堆有序
# 2nd pass: 递归利用sink()给子堆排序.

# @todo: 需要完全二叉树。好像有些长度的数组形成不了完全二叉树。例如1 2 3 4 5 6 7 8 9 一旦计算第5号元素的child
# 数组立马元素溢出. 得解决这个问题 (教材上也没解决这个问题)

## 数组下标约定:

# 注意sort,sink函数中对待数组下标是以1开始, 处理以0开始的下标的细节全部在less()和exch()函数中.不需要外部关心.
# 例如:
# l = ["S","O","R","T","E","X","A","M","P","L","E"]
# sort(1,4)就是交换S和T
# sort(2,3) 就是交换O和R

def sort(a):
    N = len(a)
    # 1st pass:
    for k in range(N // 2, 0, -1):
        sink(a, k, N)


    # 2nd pass:
    while(N>1):
        exch(a, 1, N)
        # a[N-1], a[1] = a[1], a[N-1]
        N -= 1
        sink(a, 1, N)

def sink(a, k, N):
    # l: 要操作的array
    # k: 要下沉的元素位置
    # N: array大小
    child = 2*k
    while(2 * k <= N):
        if(less(a, child, child+1)):
            child+=1
        if(not less(a, k, child)):
            break
        else:
            exch(a, k, child)
            k = child

# 比较数组的i号,j号元素,判断是否第i号小与第j号.(i是指第i个元素,不是数组下标i)
# 例如, a=['A', 'B', 'C']
# less(a,1,2) 是比较A和B!
def less(a, i, j):
    return a[i-1] < a[j-1]

# 交换数组的i号,j号元素,判断是否第i号小与第j号.(i是指第i个元素,不是数组下标i)
# 例如, a=['A', 'B', 'C']
# less(a,1,2) 是交换A和B!
def exch(a, i, j):
    a[i-1], a[j-1] = a[j-1], a[i-1]

# test
if __name__ == "__main__":
    # 
    l = ["S","O","R","T","E","X","A","M","P","L","E"]
    sort(l)