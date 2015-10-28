# insertion sort / 插入排序

# 数组被分为两部分,  
# 从后半部分的第一个元素开始, 和左边的元素挨个比较(从右到左),  如果要
# 排序的元素比左边小就交换, 然后一直往左边比较, 交换,一直到头. 这个位置的元素比较就完成, 进入下一个未排序元素的比较.




def sort(array):
    N = len(array)
    for i in range(1, N):        # 从1到N-1
        for j in range(i, 0, -1):  # 从i到1
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

def sort_alt(array):
    # 稍有不同的数组下标
    N = len(array)
    for i in range(0, N-1):        # 从0到N-2
        for j in range(i, -1, -1):  # 从i到0
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]


# test
if __name__ == "__main__":
    # 
    l1 = ["S","O","R","T","E","X","A","M","P","L","E"]
    l2 = ["S","O","R","T","E","X","A","M","P","L","E"]
    sort(l1)
    sort_alt(l2)