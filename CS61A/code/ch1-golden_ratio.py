# 体会：函数的参数是函数；
# 自顶向下的设计 先设计出improve函数的大概，它要调用哪些函数，然后再填入细节。
# 函数内部body但是可以调用函数的，但为什么要写入成参数的形式？因为这样调用这个函数的时候，形式参数就可以被替换为实际的函数，这个函数可以是变化的！


def improve(update, close, guess=1):
    """
    improvement算法

    先猜一个guess=1 然后调用uptate函数来改进guess变量，接着再用close
    函数来判断guess的值是否达到要求，不用再循环了
    """
    while not close(guess):
        guess = update(guess)
    return guess

# 其实可以看出improve函数是个通用性的函数，它不指明要解决什么问题
# 而且，我们可是甚至设计出这个函数了以后再在后面填入close  和update这两个细节性的函数，这样我们就
# 自顶向下在设计了。


def golden_update(guess):
    """
    黄金分割猜测值的更新算法
    相当于improve中的update

    """
    return 1/guess + 1

def square_close_to_successor(guess):
    """
    这个函数的作用是当guess到达某个理想值时输出true
    相当与def improve中的close

    """
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    """
    当x和y的值小于tolerance时输出true

    """
    return abs(x - y) < tolerance

# 使用：
# >>> improve(golden_update, square_close_to_successor)
# 1.6180339887498951
# 注意对这个 call exp:
# >>> improve(golden_update, square_close_to_successor)
# 求值的时候， improve(update, close, guess=1)中
# update有了argument，它是golden_update，是一个函数，close的arg是square_close_to_successor.

# 总结
# 这种把函数作为参数调用的办法有两个缺点：
# 1 是global frame里面有一大群小函数，而每个函数都必须有唯一的名字。
# 2 是update函数，作为improve函数的参数了，所以只能带一个参数。


#测试函数
from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'


improve_test()


# For this test, no news is good news: improve_test returns None after its assert statement is executed successfully.
