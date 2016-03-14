# 用邻接数组表示一个图 (无向图)
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start, visited=None):
    """ 递归版本的dfs: 获得从start点开始所有连接的顶点
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited: # 递归调用dfs算法, 起点是和start连接的一系列点.
        dfs(graph, next, visited)
    return visited

def dfs_iter(graph, start):
    """ 迭代版本的dfs . 显示地建立一个stack用来存放要搜索的点
    """
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 'A')



# def dfs_paths(graph, start, goal, path=None):
#     if path == None:
#         path = [start]
#     if start == goal:
#         yield path
#     for next in graph[start] - set(path):
#         yield from dfs_paths(graph, next, goal, path + [next])

# list(dfs_paths(graph, 'C', 'F'))

def dfs_paths_(graph, start, goal, visited=None):
    tracer = {}
    if visited == None:
        visited = set()
    if start == goal:
        return visited
    visited.add(start)
    for next in graph[start] - visited:
        trace[next] = start
        dfs_paths_(graph, next, goal, visited)


def bfs(graph, start):
    """ 找到图graph中所有和start点连接的点. 广度优先. 迭代的实现.
    """
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A')

def bfs_path(graph, start, goal):
    """
    """
    parent = {}   # a dict
    queue = [start]

    while queue:
        vertex = queue.pop()
        if vertex == goal:
            return # ..
        for next in graph[vertex]:
            parent[next] = vertex
            queue.append(next)
