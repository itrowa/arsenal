# dict
# 是key-value 的 pair. 这些pair的 order是不确定的,没有先后顺序的.尽管写起来是有先后顺序的.

######################################
# 创建
######################################
# "声明" 一个空的dict(实际是引用一个空dict)
d1 = {}

# 正常的dict的创建并用变量引用它.

numerals = {'I': 1.0, 
            'V': 5, 
            'X': 10
           }

######################################
# print 
######################################
# print
print(numerals)

######################################
# 查询 
######################################
# 取得一个Key的value:
q = numerals['X']


# 查找key是否存在：
'V' in numerals
# note: 不要使用if numeral['V'] 这样的判断,因为解释器会先去求值numeral['V']并可能返回异常

# or:
if 'V' in numerals:
    pass

# 查找value是否存在:
# ...

# 仅仅是获得dict的key名:(py3)
list(numerals.keys())[0]
# 先把所有的key名做成列表, 然后取出这个列表的第一个元素.

# 列出所有的Key:
keys = []
for key in numerals:
    keys.append(k)

numerals.items()  # 在py2下返回一个list, 在py3下返回一个view object.
list(numerals.items()) # 在py3下, 将view object做成list即可达到和python2 一样的效果了.

# In Python 2, the methods items(), keys() and values() used to "take a snap
# shot" of the dictionary contents and return it as a list. It meant that if 
# the dictionary changed while you were iterating over the list, the contents 
# in the list would not change.

# In Python 3, these methods return a view object whose contents change 
# dynamically as the dictionary changes. Therefore, in order for the behavior 
# of iterations over the result of these methods to remain consistent with 
# previous versions, an additional call to list() has to be performed in 
# Python 3 to "take a snapshot" of the view object contents.

######################################
#  修改 / 新增
######################################
# 给Key设置新的Value, 或者增加新的pair:
numerals['I'] = 1
numerals['L'] = 50
