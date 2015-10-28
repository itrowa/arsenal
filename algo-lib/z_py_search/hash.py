# 验证hash函数的均布性.
# 用python实现教材上的hash实现,是否能满足教材上所说的性质? 测试通过了才能进行下一步..

def gethash(x):
    """
    将python的hash返回值转换为我们需要的数组索引. 数组索引范围为0~(M-1), 共M个.
    """
    return (hash(x) & 0x7fffffff) % M
    # 剔除符号位.

M = 5

l = []
d = {}

# 对0~99这99个key,计算hash值, 并统计各个hash值的出现次数.
for i in range(100):
    hcode = gethash(i)
    print(hcode)
    if not hcode in d:
        d[hcode] = 1
    else:
        d[hcode] += 1

# 计算

n_key=len(d)        # dict中key的数目


def num_of_hash(d):
    h_num = 0
    for k in d:
        if d[k]:
            h_num +=  d[k]
    return h_num

for k in d:
    print("{0}:{1}".format(k, d[k]))

# 平均每个hash值出现多少次?
avg = num_of_hash(d) / n_key


# 计算


# print(gethash("S"))
# print(gethash("E"))
# print(gethash("A"))
# print(gethash("R"))
