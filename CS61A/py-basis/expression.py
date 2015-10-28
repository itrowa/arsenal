length = 5
breadth = 2
area = length * breadth
print 'Area is', area
print 'perimeter is', 2 * (length + breadth)


def welcome():
    print('welcome to')
    return 'hello'

def cs61a():
    print('cs61a')
    return 'world'

print(welcome(), cs61a())
# 用程序验证输出结果是多少?


# 关于数学表达式

# normal div
print(1/4)
print(4/2)
print(11/3)

# floor div
print(1//4)
print(4//2)
print(11//3)

# 取Mod
print(1%4)
print(4%2)
print(11%3)


def beep(x):
    print(x)

3 + beep(8)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'`


# boolean op.
a, b = 10, 6

print(a)
print(not a)
print(a != 0 and b > 5)
print(a < b or not a)
