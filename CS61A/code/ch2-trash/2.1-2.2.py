# 先假设我们可以定义rational number (以分子 / 分母的形式)
def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

#使用 List literal
"""
To enable us to implement the concrete level of our data abstraction, Python provides a compound structure called a list, which can be constructed by placing expressions within square brackets separated by commas. Such an expression is called a list literal.
"""

>>> [10, 20]
[10, 20]
[10, 20]
#访问list的element有两种方法

# 1
pair = [10, 20]
x, y = pair

#x就是10, y就是20了


#2
# list element selection operator
pair[0]
pair[1]

# list is 0-indexed, eg, index 0 select the first elemtnt, index 1 slect the second, etc.. indexing means that how far an element is offset from the beginning of the list.

#list element selection operator 的等价函数

from operator import getitem
getitem(pair, 0)


def rational(n, d):
    return [n, d]
def numer(x):
    return x[0]
def denom(x):
    return x[1]


>>> half = rational(1, 2)
>>> print_rational(half)
1 / 2

最小规约??
lowest terms


#abstraction barriers/ 抽象屏障

# 上一层的函数构建于下一层的函数, 这提供了抽象的保障. 


def pair(x, y):
    """Return a function that represents a pair."""
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get
def select(p, i):
    """Return the element at index i of pair p."""
    return p(i)

#With this implementation, we can create and manipulate pairs.

# >>> p = pair(20, 14)
# >>> select(p, 0)
# 20
# >>> select(p, 1)
# 14



#range: 生成sequence



# 一个找出perfect number的程序

def divisors(n):
    return [x for x in range(1, n) if n % x == 0]

[n for n in range(1, 1000) if sum(divisors(n)) == n]


# 下面这个程序找出一个rect的最小周长

def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)
