class Node:
    # 链表. 一个链表的节点包含item(其值)和next(指向下个链表的指针)

    # first = Node("to")
    # second = Node("be")
    # third = Node("or")

    # first.next = second
    # second.next = third

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