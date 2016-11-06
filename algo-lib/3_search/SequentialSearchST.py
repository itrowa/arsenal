# 利用(无序)链表构建有序符号表

# 实现: 使用一个无序链表, 每个node储存key和对应的value. 新加入的node插入至表头. 查找也是从表头开始寻找.

# @todo: __repr__()遇到大型数据时递归深度溢出的问题

# 一个节点含有两个属性和一个next指针的链表Node类
class Node:
    empty = ()              # 用空的tuple表示"empty"
    def __init__(self, key, value, next = empty):
        assert next is Node.empty or isinstance(next, Node)
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        if self.next:
            next_str = ' → ' + repr(self.next)
        else:
            next_str = ''
        return '[{0}|{1}]{2}'.format(self.key, self.value, next_str)



# 基于链表实现的Symbol Table类
class SequentialSearchST:

    empty = ()

    def __init__(self):
        node = Node(Node.empty, Node.empty)         # 一个哨兵node
        self.first = Node(Node.empty, Node.empty)   # 第一个Node的指针.指向刚才的哨兵node.
        self.N = 0                                  # size of ST

    def __repr__(self):
        return self.first.__repr__()

    def __getitem__(self, key):
        """ 使支持下标访问 """
        # st['C']       103
        return self.get(key)

    # 查找给定的key并返回对应的value
    def get(self, key):
        x = self.first
        while(x.key != Node.empty):
            if (x.key == key):
                return x.value
            x = x.next
        return None
            
    # 查找给定的key并更新其值, 若不在ST中则新建一个node
    def put(self, key, val):

        x = self.first
        while(x.key != Node.empty):
            if (x.key == key):
                x.value = val
                return
            x = x.next
        nod = Node(key, val, self.first)
        self.first = nod 

    def delete(self, key):
        # reset whole linked list using help func.
        self.first = self.delhelp(self.first, key)

    def delhelp(self, x, key):
        """ del a node by resetting a link list from node x"""
        if x == Node.empty:
            return None
        elif x.key == key:
            return x.next
        else:
            x.next = self.delhelp(x.next, key)
            return x

    def contains(self, key):
        return self.get(key) != None

    def size(self):
        return self.N


# test case:
if __name__ == "__main__":
    st = SequentialSearchST()
    st.put('A', 101)
    st.put('B', 102)
    st.put('B', 108)
    st.put('C', 103)
    st.get('A')
    st.get('C')
    st.put('A', 190)
    st.get('D')
    st.put('E', 198)

