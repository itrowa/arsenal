# 一个图对象.
class Graph:

    def __init__(self, V=None, stm=None):
        """
        V: 数字.
        stm: 一个iterator, 前两个元素表示V和E的大小, 后面就是一个个的node名
        要么输入V, 要么输入stm.
        """
        if stm != None:
            self.V = stm.__next__()
            self.E = stm.__next__()

            # 初始化表示相邻信息的数组
            self.adj = [None] * self.V

            # 添加node和路径
            for i  in  range(0, self.E):
                v = stm.__next__() 
                w = stm.__next__()
                self.addEdge(v, w)
        elif V != None:
            self.adj = [None] * self.V
            self.V = V
            self.E = 0
        else:
            self.adj = [None]
            self.V = 0
            self.E = 0


    def getV(self):
        return self.V

    def getE(self):
        return self.E

    def addEdge(self, v, w):
        if self.adj[v] == None:
            self.adj[v] = [w]
        else:
            self.adj[v].append(w)

        if self.adj[w] == None:
            self.adj[v] = [w]
        else:
            self.adj[w].append(v)
        self.E += 1

    def adj(self, v):
        return self.adj[v]

###########################################
# common tasks
###########################################

# 计算v的度数
def degree(G, v):
    degree = 0
    for w in G.adj(v):
        degree += 1
    return degree

# 计算所有顶点的最大度数
def maxDegree(G):
    max = 0
    for v in range(0, G.V()):
        if degree(G, v) > max:
            max = degree(G, v)
    return max

###########################################
# test routine 
###########################################

import sys
if __name__ == "__main__":

    # import graph def, from stdin, as list
    inlist = []
    for i in sys.stdin.read().split():
        inlist.append(int(i))    # 把每个元素转为int型
    inlist_iter = inlist.__iter__()

    g = Graph(stm=inlist_iter)
    print(g.V)
    print(g.getE())

