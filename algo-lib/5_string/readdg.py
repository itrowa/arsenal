# 用于处理算法一书提供的图
import sys

# 读入V和E
v_cnt = sys.stdin.readline()
e_cnt = sys.stdin.readline()

# 读入剩下的边
raw_edges = [line.split() for line in sys.stdin]

# 把元素从string类型转换为int
for pair in raw_edges:
    for i in range(len(pair)):
        pair[i] = int(pair[i])

# print 
print(v_cnt)
print(e_cnt)

for edge in raw_edges:
    s = str(edge[0]) + " → " + str(edge[1])
    print(s) 

