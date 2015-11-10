l = [1, 2, 3, 4]
l.__iter__()                        # 得到一个list iterator
l.__iter__().__next__()             # 得到next的值

##########################################
# list comprehension
##########################################

# 实质: for循环的语法糖.

# 得到一个generator object
s1 = (x*x for x in l if x >= 2)
# 是一个iterator, 也是一个iterable obj.

for i in s1:
    print(i)

# 得到一个list
list(x*x for x in l if x >= 2)
[x*x for x in l if x >= 2]

##########################################
# 利用函数
##########################################
ss = map(lambda x: x*x, l)
ss      # 一个map object   按需计算.
list(ss)   # 将其计算出来.

##########################################
# lazy computaion: eval on demand!
##########################################

r = range(5)
r.__iter__()
r.__iter__().__next__()

l