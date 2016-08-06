# 多路搜索树
class Tree:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids  # 指向其子节点
        self.next = next     # 指向其兄弟

t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
t.kids.next.next.val    # c