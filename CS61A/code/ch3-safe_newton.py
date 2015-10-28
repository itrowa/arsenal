class IterImproveError(Exception):
    # 所有的自定义exception类都必须继承自Exception类.
    # 在程序的某部分中会raise这个Error 类.
    def __init__(self, last_guess):
        self.last_guess = last_guess:

def improve(update, done, guess=1, max_updates=1000):
    # 通用的迭代式improve.函数. 它只负责测试现在的guess是否足够好, 如果不, 就继续调用update函数来改进guess.
    k = 0
    try:
        while not done(guess) and k < max_updates:
            # 还能继续改进猜测, 且猜测次数也没达到上限~
            guess = update(guess)
            k = k + 1
        return guess
    except ValueError:
        # Value Error 是py built-in的一种异常: 当built-in的函数接受对的type但value不适合时触发.
        # 触发我们自定义的那个exception. 思路是这样的, 错误的计算导致了python抛出一个自带的异常, 然后我们对这个异常的处理办法是在抛出另外一个异常IterImproveError, 而这个异常是我们自定义的, 这样handle以后, 出现异常也可以继续工作.
        raise IterImproveError(guess):

def find_zero(f, guess=1):
    # 找零点函数. 目的是求一个函数f的零点.
    def done(x):
        return f(x) == 0
    try:
        # 调用通用improve函数.
        return improve(newton_update(f), done, guess)    # newton_update() 在composing program的chapter 1
    except IterImproveError as e:
        return e.last_guess


# ###########################################
# play
# ###########################################

from math import sqrt
find_zero(lambda x: 2*x*x + sqrt(x))
