class Node:
    # 链表. 一个链表的节点包含item(其值)和next(指向下个链表的指针)
    empty = () # class attr. 用空的tuple表示empty

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
        return 'StackNode({0}{1})'.format(self.item, next_str)

class Queue:
    def __init__(self, item = None):
        if item == None:
            self.head = Node.empty
            self.tail = self.head
        else:
            self.head = Node(node)
            self.tail = self.head

    def isEmpty(self):
        return self.head == Node.empty

    def enqueue(self, item):
        if self.isEmpty():
            self.tail = Node(item)
            self.head = self.tail
        else:
            oldTail = self.tail
            self.tail = Node(item)
            oldTail.next = self.tail

    def dequeue(self):
        if self.isEmpty():
            return 'error'
        else:
            val = self.head.item
            self.head = self.head.next
            return val

# # test client.
# q = Queue()

# string = "to be or not to - be - - that - - - is"
# string = string.split() # 切分为单词的列表
# for item in string:
#     if (item != "-"):
#         q.enqueue(item)
#     else:
#         print(q.dequeue())

# print(s.size())
q = Queue()
q.enqueue('to')
q.enqueue('be')
q.dequeue()