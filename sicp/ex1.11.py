def f(n):
    """Computed recursively.

    """
    if n <= 3:
        return n
    return f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)

def f_iter(n):
    # 这实际上是两个函数， 当输入的n是1~3时，直接返回，如果是大于3的才进入下面的计算,这和题目的算法很类似。
    if n == 1 or n == 2 or n == 3:
        return n

    # 如果是大于3的数    
    # f的前3项
    f_dec3, f_dec2, f_dec1 = 1, 2, 3
    cnt = 4
    # 例如，从第4项:f(4)开始计算, f()
    while cnt <= n:
        print("---------------------------------")
        print("start from cnt", cnt)
        print("---------------------------------")
        # 把f(3)的值传给f(2), 再把f(2)的值传给f(1),最后把f(1)的值
        f_cnt = f_dec1 + 2* f_dec2 + 3*f_dec3
        print("iter done, result:", result, f_dec1, f_dec2, f_dec3)

        # 为循环的下一次迭代做准备：
        #下一次的   这一次的
        # f_dec1 = result
        # f_dec2 = f_dec1
        # f_dec3 = f_dec2
        f_dec1, f_dec2, f_dec3 = result, f_dec1, f_dec2 
        cnt = cnt + 1
    return f_cnt    

def f_iter_alt(f_cnt, f_dec1, f_dec2, cnt, n):
    ######################################
    # 同样是迭代计算的版本， 但是这个用递归来实现迭代计算。
    ######################################
    # 不超过3的数
    if n == 1 or n == 2 or n == 3:
        return n

    # 如果是大于3的数    

    # 首先决定递归终止条件，这个等价于循环的判断条件
    if cnt > n : return f_cnt


    # 不用计算计算cnt当前的一项
    #...

    # 循环过程和为下次迭代而准备的赋值过程被这个递归调用代替了:
    f_cnt = f_iter_alt(f_cnt + 2*f_dec1 + 3*f_dec2, f_cnt, f_dec1, cnt + 1, n)

    return f_cnt    

# 要计算f(5)，必须这样调用：
print(f_iter_alt(3, 2, 1, 4, 5))
# 结果应该是22