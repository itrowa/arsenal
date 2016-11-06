class Stack:
    # 利用python内置的list特性实现的Stack
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # 将一个元素压入栈
    def push(self, item):
        self.items.append(item)

    # 将元素弹出栈
    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# test client.
s = Stack()

print(s.is_empty())

string = "to be or not to - be - - that - - - is"
string = string.split() # 切分为单词的列表
for item in string:
    if (item != "-"):
        s.push(item)
    else:
        print(s.pop())

print(s.size())