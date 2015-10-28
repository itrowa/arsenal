# 关于带*的参数

def mymul(*args):
    '''
    *args的意思是，允许这个函数接受任意多的 参数，并且把它们搜集到一个元组*args中。
    所以*args是可迭代对象.
    '''

    for arg in *args:
        total = 1
        total *= arg
    return total

print(mymul(2,3))
print(mymul(2,2,2))