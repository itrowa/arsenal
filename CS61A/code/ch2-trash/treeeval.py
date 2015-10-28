from tree import *

# 用来验证partition tree的问题

t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print(t1)
print(root(t1))
print(root(t1))

print(branches(t1))
#[[1], [2, [1], [1]]]

print(root(branches(t1)[1]))
#2

t2 = tree(3, [tree(1)])
print(t2)

t3 = tree(3)
print(t3)
# >>> is_leaf(t)
# False
# 
# >>> is_leaf(branches(t)[0])
# True
print("----")
pt1 = partition_tree(3, 2)
print(pt1)
print(branches(pt1))
print("----")
print_parts(pt1)

