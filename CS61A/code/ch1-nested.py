# nested definition
# 在定义中定义

def average(x, y): 
    return (x + y)/2 
 
def improve(update, close, guess=1): 
    while not close(guess): 
        guess = update(guess) 
    return guess 
 
def approx_eq(x, y, tolerance=1e-3): 
     return abs(x - y) < tolerance 
  
def sqrt(a): 
    """ 
    注意这是一个nested defination

    """
    def sqrt_update(x): 
        return average(x, a/x) 
    def sqrt_close(x): 
        return approx_eq(x * x, a) 
    return improve(sqrt_update, sqrt_close) 
 
result = sqrt(256) 

# 在有nested defination的程序里面，求值过程中的frame模型有何不同？

# sqrt(256)这个call exp求值时，global frame里面：

# global frame:
#  sqrt -> 关联到 func sqrt(a)

# sqrt(x) frame: (上级frame: global frame)
#    x  ->   256
#    sqrt_update -> func sqrt_update(x)
#    sqrt_close -> func sqrt_close(x)
#
# 和在global frame里面一样， 如果在一个函数的定义里面又有新的def， 那么在这个函数被调用的时候创建这个函数的local frame的时候， 这个函数里面的def材料会创建绑定，当然创建的绑定也只在这个local frame里面能用，它的scope也就是sqrt(x)的这个local frame.

# 而且，我们现在要扩展一下环境模型：需要记录一下每个frame的上一级frame是什么，例如这里的sqrt(x)的frame，上级是global, 而sqrt_update(x)被调用时创建的frame，它的上级frame就是sqrt(x)的frame了。

# 另外要注意的是, 现在多个frame要有继承的概念了.例如, sqrt(x)的frame的上一级是global frame, sqrt_update(x)的frame上一级是sqrt(x)的frame. 等等

# 还要注意的是, frame的演化过程中, 当执行到sqrt_update的body部分的时候, 它是去哪里找a的值的? 首先它在当前的frame里面找是否有a绑定的值 - 当然是没有, 于是它到上级frame,也就是sqrt(a)被调用时创建的frame,发现a被绑定到256.于是采用这个值.


# lexu
