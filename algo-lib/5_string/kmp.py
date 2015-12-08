# Knuth-Morris-Pratt substring search algorithm
R = 3               # 基数(一个字符可能取的总的情况数, 这里简化为A,B,C,共3种)
dic = {
        'A': 0,
        'B': 1,
        'C': 2
        }

def getDFA(pat):
    ''' 根据一个模式pat, 利用KMP算法建立有限状态机
    '''
    l = len(pat)
    # construct dfa
    dfa = [[0 for col in range(l)] for row in range(R)]

    # 完成整个dfa表格
    X = 0                   # 用来存储一个临时 state的编号

    # 手动处理dfa第一列中应该跳转的态.
    mi = dic[pat[0]]
    dfa[mi][0] = 1

    # print(dfa)

    for j in range(1, l):
        # matched index: 对于i=0来说, pi等于A, i=1,pi=B, etc
        mi = dic[pat[j]]

        # 对一列来说, 处理这一列的所有行
        for c in range(0, R):
            dfa[c][j] = dfa[c][X]

        # 设置跳转的态为j+1
        dfa[mi][j] = j+1

        # 更新X
        # 正确输入pat[1]到pat[j]后, 机器应该属于的状态是:
        X = int(dfa[mi][X])             # @pitfall 记得显式地把结果转换为int.. 血的教训!

    return dfa

def search(pat, txt):
    """
    在字符串txt中搜索模式pat.
    返回一个数字, 表示从该数字开始后面的字符一直匹配pat.
    """
    M = len(pat)   
    N = len(txt)

    # 根据pat计算dfa.
    dfa = getDFA(pat)

    # i: 文本指针
    # j: 当文本指向i时, 已经匹配了pat的字符数
    i = 0
    j = 0
    while i < N and j < M:
        # txt的第i处字符对应的dfa所在的行号:
        subs = dic[txt[i]]

        # 更新j的值并进入下一轮迭代
        j = dfa[subs][j]
        i += 1;

    # 文本搜索完成后, 根据j的大小判断匹配是否成功
    if j == M:
        return i - M
    else:
        return N

if __name__ == "__main__":
    txt = 'ACABCACABABABACABCAAC'
    pat =          'ABABAC'
    search(pat, txt)

