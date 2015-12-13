# re: is txt matches regxp?
from digraph import *

def isMatched(txt, regexp):
    """ is txt matches this regexp?
    """
    # 思路: 1. 一开始, 进行ε跳转, 能达到的所有态记入states_togo , 
    #       2. 读入一个字符并跳转, 跳转后的所有态记为清空后的s_temp
    #       3. 进行ε跳转, 跳转后的所有态记如清空后的state_togo 
    #       重复2, 3.
    M = len(regexp)                       # len of regexp

    # 1. 到达s0的过程
    epsg = buildEpsGraph(regexp)           # epsilon transition graph
    # ε跳转.
    states_togo = findVertices(epsg, 0)
    print("states after apply ε-transitions at the first time: ", str(states_togo))


    # 2.现在逐个读入txt的字符并迭代处理:
    for i, char in enumerate(txt):
        s_temp = []  # 存储可以跳转到的状态编号.
        # 到达s1的过程:
        print('------------')
        print("reading " + char + " in txt: ")
        for v in states_togo:
            if v == M:              # 查找已经结束 这一支不用管了.
                continue
            elif ((regexp[v] == char)) or regexp[v] == '.':
                s_temp.append(v+1)
        print("states after read this char: " + str(s_temp))

        # 到达s2的过程:
        states_togo = []
        for v in s_temp:
            for result in findVertices(epsg, v):
                states_togo.append(result)
        print("states after apply ε-transitions: " + str(states_togo))

    # 函数返回值
    for v in states_togo:
        if (v == int(M)):
            return True
    return False

def buildEpsGraph(regexp):
    """ 以regexp的每一个字符为顶点, 建立ε-跳转的有向图.
        返回的图中, 顶点是编号是对应的字符在regxp中的下标
    """
    M = len(regexp)                       # len of regexp
    g = Digraph(M+1)
    ops = []                        # regexp中的(, ), *, |等元素对应的下标将记录于此.

    for i, char in enumerate(regexp):
        # a case analysis
        if char == '(':
            ops.append(i)
            g.addEdge(i, i+1)
        elif char == '|':
            ops.append(i)
        elif char == ')':
            lop = ops.pop()         # last op
            if (regexp[lop] == '|'):
                llop = ops.pop()    # last last op
                g.addEdge(llop, lop+1)
                g.addEdge(lop, i)
                g.addEdge(i, i+1)
        elif char == '*':
            g.addEdge(i-1, i)
            g.addEdge(i, i-1)
            g.addEdge(i, i+1)
    # 添加最后一条边
    g.addEdge(M-1, M)

    return g

if __name__ == "__main__":
    regexp = '((A*B|AC)D)'
    txt = 'AABD'
    print(isMatched(txt, regexp))
