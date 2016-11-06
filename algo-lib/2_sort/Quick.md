# quick sort / 快速排序

快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

步骤为：

 - 从数列中挑出一个元素，称为"主元"（pivot），
 - 重新排序数列，所有元素比主元小的摆放在主元前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
 - 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。


分区操作的特点如下：

- 原地进行分区;
- 除了pivot以外，剩余的元素会被分为两组，分组的过程是这样：如果这个元素比pivot大，则不做任何事情，如果比pivot小，则把它和左边那组最后一个比pivot小的元素右边的一个元素进行交换.注意不是插入到那，而是交换.

递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

    shuffle elements in array
    recursively sort array:
        pick first element as pivot
        for element in (array - pivot):
          if element > pivot：
             swap element, array[leftPartLastIndex+1]
          else:
             do nothing
        swap pivot, leftPartLastValue

        sort array[startIndex, pivotIndex]
        sort array[pivotIndex+1, endIndex]

循环不变式:

- 切分操作的每一次迭代开始前, array中leftPart中的元素都小于pivot
- 切分操作的每一次迭代开始前, array中leftPart+1到那个当前element的元素都大于Pivot
- array中pivit的下标处元素等于pivot  

正确性证明:

1. 程序初始化时, leftPart和rightPart都不包含任何元素. 因此满足循环不变式.
2. 每一轮迭代完后, leftPart的所有元素都小于pivot, rightPart所有元素都大于pivot. 要想清楚这一点，需要考虑每轮迭代中的两种情况： 如果当前element大于pivot, 则数组保持不变. 这个element保留在原地成为rightPart的一部分. 所以满足循环不变式. 如果当前element小于pivot, 则将这个element和leftPartLastIndex+1处的element交换. 交换完成后, leftPart部分所有的元素都小于pivot, rightPart部分所有的元素都大于pivot, 循环不变式成立.
3. 程序终止时: 略.

根据归纳原理, 程序是正确的.
