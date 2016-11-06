class UF:
    def __init__(self, N):
        self.id = [None] * N
        self.count = N          # 连通分类统计
        # 初始化索引数组. 一开始, 每个site都只和自己连通. 邻接数组?
        for i in range(N):
            self.id[i] = i

    def union(self, p, q):
        """ 在p和q之间添加一条连接 """
        int pID = find(p);
        int qID = find(q);

        # 如果p,q已经在相同的分量中, 则不需要任何操作,
        # 否则将p的分量名改为q的.
        if pID == qPD:
            return None
        else:
            for i in range(len(self.id)):
                if self.id[i] == pID:
                    self.id[i] = qID
                count -= 1

    def find(self, p):
        """ p(0~N-1)所在分量的标识符 """
        return id[p] 

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count():
        return self.count

if __name__ == "__main__":
    # 注意输入数据, 第一行是触点数量
    # 然后 每一行代表一个两个触点的连接
