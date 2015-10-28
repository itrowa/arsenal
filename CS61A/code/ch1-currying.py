def curry2(f):
    """ 返回curry化的2个参数的函数。"""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
# curry2(f)(x)(y)  equals to f(x,y)
# >>> pow_carried = curry2(pow)
# >>> pow_curried(2)(5)
# 32


def uncurry2(g):
    """Return a two-argument version of the given curried function."""
    def f(x, y):
        return g(x)(y)
    return f
# uncurry2(curry2(f)) equals to f.
