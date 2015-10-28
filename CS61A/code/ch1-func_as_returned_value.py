def square(x):
    return x * x

def successor(x):
    return x + 1

# 注意, compose1的参数是f, g，是两个函数(参见函数作为参数)，
# 
# 返回的是一个函数h!, 这个h，现在还是抽象的f(g(x)),但是当compose1被应用到2个实参后，这个函数就变得具体起来。
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h # 注意是h而不是h(x),带形参的用法是def中才有的，而call exp虽然也有类似的括号，但括号里面的是实参。

def f(x):
    """Never called."""
    return -x

# 创建一个绑定
square_successor = compose1(square, successor)
# 当compose1(square, successor)执行完后，h(x)函数就变成具体的函数了：
# 

result = square_successor(12)

# 应用环境模型的时候, 留意到compose1是由compose1(square, successor)调用的, 所以compose1的两个参数f, g是 global frame里面的 func square(x) 和 successor(x) 这两个函数, 而不是global frame 里面的f(x)这个函数


# 或者直接这样调用：
compose1(square, successor)(12)
