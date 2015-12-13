class Digraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for x in range(V)] 

    def __repr__(self):
        s = str(self.V) + " vertices, " + str(self.E) + " edges\n"
        for i in range(self.V):
            for v in self.adj[i]:
                s += str(i) + " → " + str(v) + "\n"
        return s

    def getV():
        return self.V

    def getE():
        return self.E

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.E += 1

# 利用深度优先搜索寻找图g, 从s顶点出发所能达的所有顶点.
# 如果顶点s是多个参数, 会自动被py绑定为一个tuple
# 返回的是一个list, 存储的是顶点的编号.
def findVertices(g, *sources):
    marks4v = [False] * g.V
    def dfs(g, s):
        marks4v[s] = True
        for vertice in g.adj[s]:
            if not marks4v[vertice]:
                dfs(g, vertice)
    for s in sources:
        if marks4v[s] == False:
            dfs(g, s)
    return [i for i, value in enumerate(marks4v) if value == True]

# python digraph.py < tinyDG.txt
# 注意: 这个tinyDG.txt内容和教材上的有一些不一致.
if __name__ == "__main__":
    import sys
    # 读入V和E
    v_cnt = int(sys.stdin.readline())
    e_cnt = int(sys.stdin.readline())
    # 读入剩下的边
    raw_edges = [line.split() for line in sys.stdin]
    # 把元素从string类型转换为int
    for pair in raw_edges:
        for i in range(len(pair)):
            pair[i] = int(pair[i])

    # 建立有向图
    g = Digraph(v_cnt)
    for edge in raw_edges:
        g.addEdge(edge[0],edge[1])
    print(g)

    # 查找g内, 点0可达的所有点.
    print(findVertices(g, 0))

    # 查找g内, 点0, 2可达的所有点.
    print(findVertices(g, 0, 2))

