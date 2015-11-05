# 函数是可以修改引用的.
l=[1,2,3,4,5]

print(l)

def modify(l):
    l[2] = None

modify(l)
print(l)