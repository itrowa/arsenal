class Account(object):
    # 这三个有什么区别??
    interest = 0.02 # Class attribute
    self.interest = 0.02
    Account.interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        # 能不能写成
        # balance = 0? 
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Yes!")

    # what if.. 有什么区别?
    self.interest = 0.02
    Account.interest = 0.02

# 写class的时候心中要有写"模板"的意识：
# 比如，要注意到self这个东西其实就是创建好了的instance

# 创造一个instance
a = Account("Billy")

################################
#通过一些测试来理解oop的特性
################################

Account.holder
# 出错！ 但是 why?



