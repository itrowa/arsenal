# Quick的另一种实现. 主要是partition操作的pivot的选择是选择最后一个元素. 本质上没什么差别.
def quick(a, lowIndex, hiIndex):

    # 原地分区操作.
    def partition(a, lowIndex, hiIndex):
        pivotIndex = hiIndex
        markIndex = lowIndex

        for i in range(lowIndex, hiIndex):  # 保证从第1个元素到倒数第2个元素.
            print(i)
            if a[i] < a[pivotIndex]:
                a[i], a[markIndex] = a[markIndex], a[i]
                markIndex += 1

        a[pivotIndex], a[markIndex] = a[markIndex], a[pivotIndex]

        # 切分程序中, markIndex及右边部分的元素都比pivot大.
        return markIndex

    # shuffle a omitted.
    print("sorting: ", lowIndex, hiIndex)

    if lowIndex >= hiIndex:
        return

    midIndex = partition(a, lowIndex, hiIndex)
    quick(a, lowIndex, midIndex-1)
    quick(a, midIndex+1, hiIndex)



a = ["S","O","R","T","E","X","A","M","P","L","E"]

quick(a, 0, len(a)-1)   # sort: 下标从0到10