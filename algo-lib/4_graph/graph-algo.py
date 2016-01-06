# 常见的无向图和有向图算法.

# 用邻接数组表示一个图 (无向图)
g2 = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

g1 = { 0: [2, 1, 5],
       1: [0, 2],
       2: [0, 1, 3, 4],
       3: [5, 4, 2],
       4: [3, 2],
       5: [3, 0]}

g3 = { 0: [6, 2, 1, 5],
       1: [0],
       2: [0],
       3: [5, 4],
       4: [5, 6, 3],
       5: [3, 4, 0],
       6: [0, 4],
       7: [8],
       8: [7],
       9: [11, 10, 12],
       10: [9],
       11: [9, 12],
       12: [11, 9]
       }

###############################################################

def v(graph):
    """ 计算graph的顶点数
    """
    return len(list(graph.keys()))

def dfs(graph, start, visited=None):
    """ 递归版本的dfs: 获得从start点开始所有连接的顶点
    """
    if visited is None:
        visited = []
    visited.append(start)

    for next in graph[start]: # 递归调用dfs算法, 起点是和start连接的一系列点.
        if next not in visited:
            dfs(graph, next, visited)
    return visited

dfs(g1, 0)

def bfs(graph, start):
    """ 找到图graph中所有和start点连接的点. 广度优先. 迭代的实现.
    """
    visited = [start]
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        for next in graph[vertex]:
            if next not in visited:
                queue.append(next)
                visited.append(next)
    return visited

def bfs_alt(graph, start):
    """ never works!
    """
    visited = []
    queue = [start]

    while(queue):
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
        for next in graph[vertex]:
            queue.append(next)


bfs(g1, 0)
bfs(g2, 'A')

def bfs_path(graph, start, goal):
    """ 求图graph中从start点到goal点的路径.
    """
    parents = {}   # a dict. 每个顶点的value记录着它的前一个顶点. 实际上得到一个backtrace tree.
    queue = [start]
    visited = [start]

    def backtrace(parents, start, end):
        """ 根据parents树提供的路径, 求从start点到end点的路径
        """
        path = [end]
        while path[-1] != start:
            path.append(parents[path[-1]])
        path.reverse()
        return path

    while queue:
        vertex = queue.pop(0)
        if vertex == goal:
            return backtrace(parents, start, goal)
        for next in graph[vertex]:
            if next not in visited:
                parents[next] = vertex
                visited.append(next)
                queue.append(next)

bfs_path(g1, 0, 5) # [0, 5]
bfs_path(g1, 0, 3) # [0, 2, 3]


def cc(graph):
    """ 计算一幅图的连通分量
    """
    visited = []
    components = []
    ci = 0

    def dfs_mark(graph, s):
        visited.append(s)
        components[ci].append(s)
        for next in graph[s]:
            if next not in visited:
                dfs_mark(graph, next)

    for v in list(graph.keys()):
        if v not in visited:
            components.append([])
            dfs_mark(graph, v)
            ci += 1
    return components


cc(g3)
# [[0, 6, 4, 5, 3, 2, 1], [7, 8], [9, 11, 12, 10]]