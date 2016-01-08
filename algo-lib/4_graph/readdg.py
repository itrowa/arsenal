# 用于处理算法一书提供的图数据, 最后生成的是简单的python邻接list
# 还未完成.
# python readdg.py < tinyG.txt
import sys

# 读入V和E
v_cnt = sys.stdin.readline()
e_cnt = sys.stdin.readline()

# 读入剩下的边
raw_edges = [line.split() for line in sys.stdin]

# 把元素从string类型转换为int
for pair in raw_edges:
    if not pair: # 如果pair是[]
        raw_edges.remove([])
    for i in range(len(pair)):
        pair[i] = int(pair[i])

print(raw_edges)
# print 
print(str(v_cnt) + str(e_cnt))
for edge in raw_edges:
    s = str(edge[0]) + " → " + str(edge[1])
    print(s) 

# 生成graph
graph = {}
for edge in raw_edges:
    if edge[0] not in graph:
        graph[edge[0]] = []
        graph[edge[0]].append(edge[1])
    else:
        graph[edge[0]].append(edge[1])
print(graph)

# 一个simGraph类的草稿
class simpleGraph:
    """ 用字典来表示邻接表. 邻接表来表示一个图.
        创建好的图是这样的:
        g.data= 
        {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
    """
    def __init__(self):
        data = {}

    def addEdge(self, pair):
        """ 添加一条边, pair是一个有两个顶点组成的列表.
        """
        data[pair[0]] = pair[1]

