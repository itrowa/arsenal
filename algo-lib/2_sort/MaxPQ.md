# Max Priority Queue

# API

	insert(v)		# inseret an item
	delMax()		# return & del Max item
	Max()			# return max item(return min item if it\'s a min priority Queue)
	size()			# get size

# (elementry) unordered array implementation

# 循环不变式：一个PQ数据结构在创建后，插入元素后，删除元素后，N的数量总是等于数组中已有元素的数量,N总是指向数组中的最后一个元素。
data: MaxPQ
    data = []
    N = 0

    insert(v):
        data[N] = v
        N = N+1 

    delMax():
        max = 0
        for item in data:
            if max < item:
                max = item
            exchange data[N], item
            N = N - 1

# binay heap

用数组来表达的二叉树。且二叉树是有序的。根节点总是大于两枝。

根节点和子节点间的数组下标关系

 - 整棵树根节点下标是1
 - 若某节点下标是k, 子节点下标是2k, 2k+1.
 - 节点下标是k, 则其父节点下标是 k / 2.   (4/2=2; 5/2=2)

# 有序性
因为binary heap是用数组实现，因此在删除，插入元素时，可能打断这种有序性。下面是解决办法

## Promotion
当Child比Parent大时，需要将Child元素上浮。

    promotion for data[k]:
        while k > 1:   # k不能是根节点, 否则就不能上浮了.
            if k < data[k/2]:
                exchange data[k], data[k/2]
                k = k/2
            else: 
                break
    
循环不变式： 每次交换完成后，k所在的父节点总是大于k处节点，从而保证了k的父节点，子树，子子树的有序性.

## Demotion

当Parent比至少一个child小时，将需要将此parent下沉至有序为止.
和子节点中较大的那个交换即可.

    Demotion for data[k]:
        while 2k <= n: #n不能是leaf.
            if data[2*k] < data[2*k+1]:
                exchange data[k], data[2k+1]
                k = 2*k+1
            else:
                exchange data[k], data[2k]
                k = 2*k


# Binary Heap实现的Priority Queue

 - c: 正常创建
 - insert item: 添加到数组末尾， 然后执行promotion操作;
 - del max item: 将max item(第一个元素) 和N处的元素互换， 然后将N-1. 最后下沉掉刚刚被换到根节点的那个元素.
        

# heapsort

先建立一个数组，元素大小是随机排列的。然后把它改造成二叉堆，排序问题就解决了。

建立步骤：
1. 假设数组是N个元素，对下标是N/2到1的元素先后进行Demotion操作. 这一步完成以后，作为二叉堆的数组是有序的.(作为数组来说还是非有序的.)
2. 依次移除最大的元素。数组的末尾不断接收到这些被移除的元素，因此二叉堆排空时，整个数组就有序了。
 这一步的具体方法如下：
  只要heap还不为空：
  1. 将heap末尾的元素和heap的第一个元素交换
  2. 将刚刚交换到heap=顶的元素进行下沉
  3. 将heap的N减去1(相当于heap最末元素被删掉。)
