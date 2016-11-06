# 使用LinkedList实现FIFO队列.

# 单个节点的表示.
class Node:
    empty = () # class attr. 用空的tuple表示empty
    # can be treated as sentinel.

    def __init__(self, item, next = empty):
        """ init a node """
        # 必须先检查next也是Node类的或者next是我们的empty.
        assert next is Node.empty or isinstance(next, Node)
        # 设定两个instance attr.
        self.item = item;
        self.next = next;

    def __repr__(self):
        """ 它实现Node类的repr()函数 """
        # 先处理next部分的~
        if self.next:
            # 如果next部分存在, 递归处理它的后面部分
            next_str = ', ' + repr(self.next)
        else:
            # 如果next部分不存在, 直接为空字符串就行
            next_str = ''
        return 'Node({0}{1})'.format(self.item, next_str)

class LinkedList:
    def __init__(self):
        node = Node(Node.empty)    # 创建第一个node 它作为哨兵.
        self.first = node;	  # 链表为空的状态是: 链表内只有一个哨兵node.
        self.last = node;
        self.N = 0;

    def isEmpty(self):
        return self.N == 0

    def enqueue(self, item):
        # 注意区分链表为空和非空的情况.
        if self.isEmpty():
            self.first.item = item
            self.N += 1
        else:
            node = Node(item)
            self.last.next = node
            self.last = node
            self.N += 1

    def dequeue(self):
        # same as pop
        if self.isEmpty():
            raise Exception('LinkedList instance is empty!')
        elif self.N == 1:
            value = self.first.item
            self.first.item = Node.empty
            self.N -= 1
            return value
        else:
            value = self.first.item
            self.first = self.first.next
            self.N -= 1
            return value

    def delete(self, item):     # @?@ not tested
        """ 删除从链表头遇到的第一个名为item的元素 """
        currentNode = self.first

        while currentNode.item != Node.empty:
            if currentNode.item == item:
                currentNode = currentNode.next
                return True
        return False

    def deleteRec(self, item):
        """ 递归版本的元素删除."""
        deleteRecCore(self, item, self.first)

    def deleteRecCore(self, item, node):
        if node == Node.empty:
            return False
        elif item == node.item:
            item = item.next
            return True
        else: 
            deleteRecCore(self, item, node.next)

    def iterate(self, item):
        """ 遍历并打印所有元素. """

if __name__ == "__main__":
    # test code.
    # 从标准输入流中读入一系列字符, 如果是-则pop, 如果是非- 则push进去.
    # usage: python LinkedList.py < tobe.txt

    import sys
    lst = LinkedList()
    # 从标准输入流读入字符.
    chars = sys.stdin.read().split() # get a chars list

    for c in chars:
        if c != "-":
            lst.enqueue(c)
        else:
            print(lst.dequeue())
    print("({0} left on LinkedList)".format(lst.N))