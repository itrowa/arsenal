class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

# 创建instances
a = Account('Kirk')
b = Account('Spock')

# 访问instance attributes
a.holder
a.balance

b.balance = 200
[acc.balance for acc in (a, b)]

# 如何调用class中写好的功能？ 两种办法.class中的method与普通函数方法.
Account.deposit(spock_account, 1001)  # The deposit function takes 2 arguments
# 1011
spock_account.deposit(1000)           # The deposit method takes 1 argument
# 2011


# 2个对象虽然由同一个class调用而创建，但是这两个对象是独立的。
print(" ----------------independent objects-------------")
no1 = Account('Jim')
no2 = Account('Jack')

no1 is no1
no1 is not no2
no3 = no1
no3 is no1

# 使用对象中的methods,使用dot notation

tom_account = Account('Tom')
tom_account.deposit(100)
# 100
tom_account.withdraw(90)
# 10
tom_account.withdraw(90)
# 'Insufficient funds'
tom_account.holder
# 'Tom'

# 当这句话
# tom_account.deposit(100)
# 调用的时候，这个object 也就是tom_account有两个作用： 
# 1是决定withdraw是什么： withdraw不是env中的一个name，而是Account下的一个local name.
# 2，tom_account被绑定到self这个参数上了。


# dot notation 和 message passing
# 使用getattr来等价完成dot notation的功能
getattr(tom_account, 'balance')
#上面这一句和下面这一句等价
tom_account.balance
