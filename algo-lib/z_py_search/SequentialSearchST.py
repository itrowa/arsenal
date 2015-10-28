# 利用(无序)链表构建有序符号表

# 实现: 使用一个无序链表, 每个节点储存一对key和value.新加入的key-value对插入至表头. 查找也是从表头开始寻找.

# 难点: 基本没有, 会写链表就行, 注意删除操作.

# @todo: delete方法和其他api, __repr__()遇到大型数据时递归深度溢出的问题
#        能不能创建一个空的 或者实现只声明 而没有实际内容的效果? 散列表就可以创建空的表.

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

    def __init__(self, key, value):
        self.node = Node(key, value)

    def __repr__(self):
        return self.node.__repr__()

    def __getitem__(self, key):
        """
        使支持下标访问
        """
        # st['C']       103
        return self.get(key)

    # 查找给定的key并返回对应的value
    def get(self, key):
        x = self.node
        while(x != Node.empty):
            if (x.key == key):
                return x.value
            x = x.next
        return None
            
    # 查找给定的key并更新其值, 若不在ST中则新建一个node
    def put(self, key, val):
        x = self.node
        while(x != Node.empty):
            if (x.key == key):
                x.value = val
                return
            x = x.next
        newNode = Node(key, val, self.node)
        self.node = newNode

    def delete(self, key):
        self.put(key, None)

    def contains(self, key):
        return self.get(key) != None


# test case:
if __name__ == "__main__":
    st = SequentialSearchST('A', 101)
    st.put('B', 102)
    st.put('B', 108)
    st.put('C', 103)
    st.get('A')
    st.get('C')
    st.put('A', 190)
    st.get('D')
    st.put('E', 198)

