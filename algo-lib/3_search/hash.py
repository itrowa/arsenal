# 验证hash函数的均布性.
# 用python实现教材上的hash实现,是否能满足教材上所说的性质?

def gethash(x, M=5, R=26):
    # M: 要散列到的范围.
    # R:字母数: 这里默认为26

    hash = 0
    if isinstance(x, int):
        hash = x % M
    elif isinstance(x, str):
        for i, char in enumerate(x):
            hash = (R * hash + ord(char)) % M       # ord: get ASCII val of the char
    return hash
    # 剔除符号位.

def intTest(end):
    # 测试整数的hash, 从0到end

    keyCounts = {}  # hash key count
    # 对0~99这99个key,计算hash值, 并统计各个hash值的出现次数.
    for i in range(100):
        h = gethash(i)
        if not h in keyCounts:
            keyCounts[h] = 1
        else:
            keyCounts[h] += 1

    keyCount = len(keyCounts)        # dict中key的数目

    # 打印每一个key以及出现的次数.
    for key in keyCounts:
        print("{0}: {1}".format(key, keyCounts[key]))

def strTest(l):
    # 测试一个word列表散列后的均布性.

    keyCounts = {}
    for word in l:
        h = gethash(word, R=26, M=97)
        if not h in keyCounts:
            keyCounts[h] = 1
        else:
            keyCounts[h] += 1

    for key in keyCounts:
        print("{0}: {1}".format(key, keyCounts[key]))

if __name__ == "__main__":
    # use: python hash.py < tale.txt
    import sys
    l = sys.stdin.read().split()
    strTest(l)
