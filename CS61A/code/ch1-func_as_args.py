# 函数作为参数

def sum_naturals(n):

   return total

def sum_cubes(n):

def pi_sum(n):

# 3个函数具有相似性。 为什么不考虑简化一下呢？

# 如何应用环境模型来解读这个程序呢?

def summation(n, term): 
    """ 通用性的summation函数，注意term是一个函数"""
    total, k = 0, 1 
    while k <= n: 
        total, k = total + term(k), k + 1 
    return total 
 
def cube(x): 
    return x*x*x 
 
def sum_cubes(n): 
     return summation(n, cube) 
  
result = sum_cubes(3) 

# 注意执行到 total = total + term(k)的时候， term(k)是怎么被求值的？ 首先term(k)是一个call exp. term的值是cube函数, k的值是1! 接下来就是对cubx(x)应用参数1就行了。
