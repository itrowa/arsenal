class Queue:
    # 利用python内置的list特性实现的Queue (FIFO)
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # 将一个元素加入队列
    def enqueue(self, item):
        self.items.append(item)

    # 将元素从队列移出
    def dequeue(self):
        self.items.pop(0)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# test client.
q = Queue()

print(q.is_empty())

string = "to be or not to - be - - that - - - is"
string = string.split() # 切分为单词的列表
for item in string:
    if (item != "-"):
        q.enqueue(item)
    else:
        print(q.dequeue())

print(s.size())