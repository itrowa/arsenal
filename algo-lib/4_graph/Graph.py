class Graph:
    # V: 数字.
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [None] * self.V
        for v in range(0, self.V):
            self.adj[v] = []

    # 读入图.
    def Graph(self, info):
        self.E = info
        for i  in  range(0, self.E):
            # 添加一条边
            v = info.readInt() #??
            w = info.readInt()
            self.addEdge(v, w)

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
    if sys.argv[1]:
        data = sys.argv[1] 
        for i in data: 
            print(i)