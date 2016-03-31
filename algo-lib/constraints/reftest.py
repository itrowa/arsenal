# 测试python中的引用和赋值
class com:
    def __init__(self, l):
        self.l = l

    def alter(self):
        self.l.append("hah")

l = ["abb", "cdd"]
print(l)
c = com(l)
c.alter()
print(c.l)
print(l)
