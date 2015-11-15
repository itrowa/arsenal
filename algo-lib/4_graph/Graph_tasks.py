# 计算v的度数
def degree(G, v):
    int degree = 0;
    for w in G.adj(v):
        degree += 1
    return degree
