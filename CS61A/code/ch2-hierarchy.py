def fib(n):
    """ 返回斐波那契数

    >>> fib(20)
    6785
    """
    # 根据定义即可
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

def count(f):
    # 传入一个函数f, 它将能执行f,并记录f执行了多少次.
    # 例如, 有一个返回第n个斐波那契数的函数fib(n)
    # >>> cnted_fib = count(fib)
    # >>> cnted_fib(20)
    # >>> cnted_fib.call_count
    # 将返回它被执行过的次数.
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

def memo(f):
    """ 返回一个函数, 这个函数和f有一样的功能, 但是记住了f执行过的参数的返回值.
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
    >>> counted_fib = count(fib)
    >>> fib  = memo(counted_fib)
    >>> fib(20)
    6765
    >>> counted_fib.call_count
    21
    >>> fib(35)
    9227465
    >>> counted_fib.call_count
    36
    """
    # 将记忆存储在一个字典里面
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
        return memorized
