# python 中list的表达形式
digits = [1, 8, 2, 8]

# 当运算符作用于list的时候, 例如 +, *,，它处理的不是list中的元素，而是list自身！
[2, 7] + digits * 2

# 利用多重赋值访问list中的元素
x, y, z, r = digits

# 元素是否存在?
8 in digits
# note: 不要用if not digits[8]

# 删除某些元素
del digits[2]

# 删除制定下标的元素

# 删除具有指定值的元素

# list element selection 
pair[0]
pair[1]

# enumerate
for i, digit in enumerate(digits):
    print(i, digit)
# 0 1
# 1 8
# 2 2
# 3 8

# list中的元素也可以是list:
pairs = [[10, 20], [30, 40]]

print(pairs[1])
# [30, 40]
 
print(pairs[1][0])
# 30

# 一个奇怪的特性？
lst = [1, 2, 9, 'oski', 'bear']
lst[1:3] = [2, 3, 4, 5, 6, 7, 8]
# 现在list的值是 [1, 2, 3, 4, 5, 6, 7, 8, 'oski', 'bear']


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