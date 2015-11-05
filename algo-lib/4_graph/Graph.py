# 一个图对象.
class Graph:

    # V: 数字.
    # stm: 一个iterator, 前两个元素表示V和E的大小, 后面就是一个个的node名
    # 要么输入V, 要么输入stm.
    def __init__(self, V=None, stm=None):
        if stm not None:
            self.V = stm.__next__()
            self.E = stm.__next__()

            # 初始化表示相邻信息的数组
            self.adj = [None] * self.V

            # 添加node和路径
            for i  in  range(0, self.E):
                v = stm.__next__() 
                w = stm.__next__()
                self.addEdge(v, w)
        elif V not None:
            self.adj = [None] * self.V
            self.V = V
            self.E = 0
        else:
            self.adj = [None]
            self.V = 0
            self.E = 0

    def V(self):
        return self.V

    def E(self):
        return self.E

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def adj(self, v):
        return self.adj[v]

if __name__ == "__main__":
    import sys
