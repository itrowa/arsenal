# 本代码介绍的是python 内置的序列的用法.

# 好像不能叫做constructor. 这里. 按照书上的说法, 只是展现一些sequence abs., bahavior等等
# ####################################
# tuple
# ####################################

digits = (1, 8, 2, 8)

# length 和 element selection
len(digits)
digits[3]

# 相加, 相乘
(2, 7) + digits * 2
# (2, 7, 1, 8, 2, 8, 1, 8, 2, 8)

# tuple unpacking
d0, d1, d2, d3 = digits


# ####################################
# list
# ####################################


# python 中list 的constructor
digits = [1, 8, 2, 8]

# list 的length和element selection:
len(digits)
digits[3]


# 当运算符作用于list的时候, 例如 +, *,，它处理的不是list中的元素，而是list自身！
[2, 7] + digits * 2

# list中的元素也可以是list(闭包结构)_
pairs = [[10, 20], [30, 40]]

print(pairs[1])
print(pairs[1][0])

# for 循环
# ...

# unpacking的 for 循环
# ...

# slicing.
# ...

# 介绍两个operator： in 和 not in 
>>> digits
[1, 8, 2, 8]
>>> 2 in digits
True
>>> 1828 not in digits
True

# #######################################
# string
# #######################################


# #######################
# 如何构造一个string

city = 'berkeley'

'I am string'

"I've go an apostrophe"

""" The Zen of Python 
claims, Readability count...
"""

'The Zen of Python\nclaims, "Readability counts."\nRead more: import this.'

# 还可以使用str()函数创建string.
# str()函数的用法·：它把参数中的表达式的值计算出来，然后转换为string类型。
str(2) + ' is an element of ' + str(digits)
# '2 is an element of [1, 8, 2, 8]'

# #######################
# 最重要的两个behavior: length和element selection:
len(city)
city[3]

# #######################
# 四则运算符作用于str类型会发生什么?
'Berkeley' + ', CA'
'shabu' * 2

# #######################
# in 和 not in
'here' in "Where's Waldo?"
# 竟然会返回True



