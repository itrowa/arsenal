# 创建
# ########################################

# python 中list的创建
digits = [1, 8, 2, 8]

# list 和 list的二元运算
[2, 7] + digits * 2
# [2, 7, 1, 8, 2, 8, 1, 8, 2, 8]

# 访问元素
# #########################################

# 利用多重赋值访问list中的元素
x, y, z, r = digits

# 用下标来选择元素.
digits[0]
digits[1]

# 元素是否存在?
8 in digits
# 返回True或者False
# note: 不要用if not digits[8]

# 插入元素
# #########################################
digits.append(5)
# digits[6] = 6 # 出触发异常！数组下标越界.


# 删除元素
# #########################################

# 按下标删除元素
del digits[2]


# 删除具有指定值的元素
digits.remove(2)
# digits中的2被删除了
# 会删除找到的第一个具有此值的元素.

# 遍历
# #########################################

# enumerate
for i, digit in enumerate(digits):
    print(i, digit)
# 0 1
# 1 8
# 2 2
# 3 8

# 多维list
# #########################################

# list中的元素也可以是list:
pairs = [[10, 20], [30, 40]]

print(pairs[1])
# [30, 40]
 
print(pairs[1][0])
# 30

# misc
# #########################################

# 一个奇怪的特性？
lst = [1, 2, 9, 'oski', 'bear']
lst[1:3] = [2, 3, 4, 5, 6, 7, 8]
# 现在list的值是 [1, 2, 3, 4, 5, 6, 7, 8, 'oski', 'bear']


# iterable
# #########################################

# list是iterable的.
counts = [0,1,2]
# 调用counts的__iter__()方法得到一个iterator object:
i=counts.__iter__()
i
# <list_iterator object at 0x0000000002D15198>
i.__next__()
# 0
i.__next__()
# 1
i.__next__()
# 2
i.__next__()
# Traceback (most recent call last):
# StopIteration



# note: [] [None]
# 是不同的. []是空的数组 [None]是分配了空元素的数组.