# insertion sort / 插入排序

# 数组被分为两部分,  左边部分是排好序的, 右边部分是没排好序的.
# 排序的时候, 从右边部分第一个元素开始, 逐个和左边元素(先和左边元素的最右一个)进行比较, 然后放到合适的位置, 完成这个元素的排序.



def sort(array):
    N = len(array)
    for i in range(1, N):        # 从1到N-1
        for j in range(i, 0, -1):  # 从i到1
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

def sort_1(array):
    # 稍有不同的数组下标
    N = len(array)
    for i in range(0, N-1):        # 从0到N-2
        for j in range(i, -1, -1):  # 从i到0
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]

########################

def sort_2(array):
    # 算法导论上面的代码
    N = len(array)
    for i in range(1, N):
        key = array[i]
        j = i-1
        while(array[j] > key) and j > -1:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key

def sort_3(array):
    # 算法导论练习, 将数组元素按非升序排列(左边元素不会比右边的更小)
    N = len(array)
    for i in range(1, N):
        key = array[i]
        j = i-1
        while(array[j] < key) and j > -1:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key



# test
if __name__ == "__main__":
    # 
    l = ["S","O","R","T","E","X","A","M","P","L","E"]
    l1 = l.copy()
    l2 = l.copy()
    l3 = l.copy()
    sort(l)
    sort_1(l1)
    sort_2(l2)
    sort_3(l3)
    print(l)
    print(l1) 
    print(l2)
    print(l3)