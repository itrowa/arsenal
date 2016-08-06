# 使用列表表示树
listt = [["a", "b"], ["c"], ["d", ["e", "f"]]]
listt[0][1]    # b
listt[2][1][0] # e

# 如果我们能确定tree的子节点数目：
class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

t = Tree(Tree("a", "b"), Tree("c", "d"))
t.right.left