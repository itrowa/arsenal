def average(x, y):
    return (x + y) / 2

def sqrt_update(x, a):
    return average(x, a/x)

# 包装一下

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve (sqrt_update, sqrt_close)

# 这样干的好处： 只有一个def，不会有那么多函数名称来污染Local frame
