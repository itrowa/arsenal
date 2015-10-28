withdraw = make_withdraw(100)

def make_withdraw(balance):
    """
    Return a withdraw function that draws down balance with each call.
    这是个高阶函数: 返回函数的函数。
    """
    def withdraw(amount):
        nonlocal balance                 # Declare the name "balance" nonlocal
        # 注意这是py3 新增的关键字
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount       # Re-bind the existing balance name
        return balance
    return withdraw

wd = make_withdraw(20) 
wd(5) 
wd(3) 

# 函数解读：见onenote
# 
# 
# 如果去掉nonlocal，是会报错的。因为python有一个限制，在func body里面，一个name的所有instance必须绑定到同一个frame里面去。如果这条不成立的话，那么一个frame里面的name就有可能被多个同一个函数的不同frame所访问。
# 但还是没懂哪里违反了。。
def make_withdraw(balance): 
    def withdraw(amount): 
        if amount > balance: 
            return 'Insufficient funds' 
        balance = balance - amount 
        return balance 
    return withdraw 
 
wd = make_withdraw(20) 
wd(5) 


# python会预处理body中的所有语句才开始执行； 所以，balance = balance - amount这一句表示着balance的所有引用都必须在这个local frame里面了。if amount > balance中的balance自然是未定义的了。如果没有balance = balance - amount这一句，我想应该balance会直接去上一级frame里面找balance的值。
