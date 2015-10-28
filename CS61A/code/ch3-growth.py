#

"""
算法复杂度分析.
"""

from math import sqrt


# ############################
# 用于分析growth的辅助函数
# ############################

def count(f):
    """Return a counted version of f with a call_count attribute.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.call_count
    21891
    """
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

def count_frames(f):
    """Return a counted version of f with a max_count attribute.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count_frames(fib)
    >>> fib(20)
    6765
    >>> fib.open_count
    0
    >>> fib.max_count
    20
    >>> fib(25)
    75025
    >>> fib.max_count
    25
    """
    def counted(n):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

def fib(n):
    """The nth Fibonacci number.

    >>> fib(20)
    6765
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

# ############################
# 分析这些函数的算法复杂度
# ############################

# fibonacci 

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) +  fib(n - 1)

# exponentiation

def exp(b, n):
    """
    计算b的n次幂
    """
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)

def exp_fast(b, n):
    """
    计算b的n次幂, 快速
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)

def square(x):
    """
    计算x的平方
    """
    return x*x

# overlap

def overlap(a, b):
    """
    统计同时出现在a和b中的元素个数
    """
    count = 0
    for item in a:
        if item in b:
            count += 1
    return count


# factors

def factors(n):
    """
    计算整数n的因子
    """
    total = 0
    for k in range(1, n+1):
        if divides(k, n):
            total += 1
    return total

def factors_fast(n):
    """
    计算整数n的因子, 快速版
    """ 
    total = 0
    k = 1
    sqrt_n = sqrt(n)
    while k < sqrt_n:
        if divides(k, n):
            total += 2
        k += 1
    if k*k == n:
        total += 1
    return total

def divides(k, n):
    """ 
    测试k是否能整除n.
    """
    return n % k == 0