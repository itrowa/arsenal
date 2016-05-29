# 根据伪代码翻译过来的. 算法的构思, 证明和理解都在伪代码中完成, 这里只是翻译成机器能用的代码.
def quick(a, lowIndex, hiIndex):

    # 原地分区操作.
    def partition(a, lowIndex, hiIndex):
        pivotIndex = lowIndex
        leftPartLastIndex = lowIndex

        for i in range(lowIndex+1, hiIndex+1):  # 保证从第二个元素到最后一个元素.
            if a[i] < a[pivotIndex]:
                a[i], a[leftPartLastIndex+1] = a[leftPartLastIndex+1], a[i]
                leftPartLastIndex += 1

        a[pivotIndex], a[leftPartLastIndex] = a[leftPartLastIndex], a[pivotIndex]
        # print (a)
        return leftPartLastIndex

    # shuffle a omitted.
    print("sorting: ", lowIndex, hiIndex)

    if lowIndex >= hiIndex:
        return

    midIndex = partition(a, lowIndex, hiIndex)
    quick(a, lowIndex, midIndex-1)
    quick(a, midIndex+1, hiIndex)



a = ["S","O","R","T","E","X","A","M","P","L","E"]

quick(a, 0, len(a)-1)
