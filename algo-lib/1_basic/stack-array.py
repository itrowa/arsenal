class Stack:
    # 利用固定大小的"数组"来实现Stack.

    # 利用数组的思维模式来实现Stack. (数组用python的list来模拟)
    # 利用list, 咳咳(有点自欺欺人) 把list想象成可以mutable但是不能改变长度的array就行..
    # 也就是说self.l没有len(), pop(), push()....

    # 关于数组的下标：
    # 1. 不使用[0]，而是从1开始
    # 2. latest元素放在数组后面(下标增大的方向.)

    def __init__(self, cap):
        self.l = [None] * cap       # python用于初始化长度为cap的空list("数组")的语法
        self.N = 0                  # size of Stack, 注意这个不等于实际的数组长度.
        self.cap = cap              # 初始化时数组的长度.

    def __repr__(self):
        return self.l.__repr__()

    def isEmpty(self):
        return (self.l == [])

    # push
    # latest元素加在数组后面.
    def push(self, item):
        self.l[self.N+1] = item
        self.N += 1

    def pop(self):
        item = self.l[self.N]
        self.l[self.N] = None           
        self.N -= 1
        return item

    def size(self):
        return N


s = Stack(10)
s.push(1)
s.push(2)
s.push(3)