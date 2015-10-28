# 一个Account类
class Account:
    """A bank account that has a non-negative balance."""
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

 
# CheckingAccount is-a Account
class CheckingAccount(Account): # 多出的括号表达式表示它继承至Account类
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)


# checking = CheckingAccount('Sam')
# checking.deposit(10)
# 10
# checking.withdraw(5)
# 4
# checking.interest
# 0.01

# 应该注意的细节：
# 
# 对于deposit来说，python首先在instgance中找这个name，然后再CheckingAccount中找，最后在Account中找，Account是定义deposit的地方。
# 
# 根据dot exp的求值规则，既然deposit是一个func，在checking实例的class中找到的，dot exp求值得到一个bound method value.而这个method的参数是10.  这个调用过程调用的是deposit method，其中self绑定到checking object, amount绑定到了10.
# 
# deposit虽然是在Account 这个class中定义的，deposit是被self调用的，self是绑定到一个CheckingAccount的实例上，而不是Account上。。
# 


# Multiple Inheritance

class SavingAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return  Account.deposit(self, amount - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount, SavingAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1
