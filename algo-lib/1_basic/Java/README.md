# stack, queue, bag

## stack

### 数组实现

这里先实现了一个最简单的算法，然后使用动态数组改进掉它，最后，演示了如何支持Java的参数化类型和支持迭代访问.

`FixedCapacityStackOfStrings`

缺点:会发生上溢和下溢.

`ResizingArrayStackOfStrings`

改进: 改进垃圾回收,避免loitering

`ResizingArrayStack`

改进：使用了参数化类型.
待做：支持迭代访问.

### 链表实现

`LinkedStack`

支持的特性：泛型；支持迭代访问.

## queue

使用linkedList实现: 入列是从链表尾, 出列是从链表头.


# 隐含在其中的数据结构

如果选择使用链表实现stack, queue, bag, 那么要考虑如下问题:

push 
pop 
遍历
删除一个具有特定值的元素
...
