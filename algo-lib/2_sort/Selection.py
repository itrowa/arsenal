# selection sort / 选择排序(冒泡排序) (升序)

# 把数组分为两部分, 前半部分是已排序的, 后半部分是未排序的. 
# 刚开始只有后半部分, 所以先从0号元素开始依次比较所有在它后面的元素, 
# 对于索引为0的元素来说, 遍历所有后面的元素,找出最小的,若0处元素比最小的还大,
# 则交换, 索引0处的元素就排序完毕, 然后继续处理索引为1, 2处的..

# 对list"数组"排序

def sort(array):
    N = len(array)
    for i in range(N):
        for j in range(i+1, N):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]




# test
if __name__ == "__main__":
    # 
    l = ["S","O","R","T","E","X","A","M","P","L","E"]
    sort(l)